import re


class ExpenseTracker:
    def __init__(self, file_path: str):  # конструктор класса
        self.file_path = file_path

    def show_balance(self) -> None:  # показать баланс
        income = 0
        expenses = 0
        with open(self.file_path, 'r') as file:
            for line in file:
                record = line.strip().split(',')
                amount = float(record[2])
                if record[1] == 'Доход':
                    income += amount
                elif record[1] == 'Расход':
                    expenses += amount
        balance = income - expenses
        print(f"Текущий баланс: {balance}\nДоходы: {income}\nРасходы: {expenses}")

    def add_record(self) -> None:  # добавить запись
        date = input("Введите дату (ГГГГ-ММ-ДД): ")
        # Проверка формата даты (ГГГГ-ММ-ДД)
        if not re.match(r"\d{4}-\d{2}-\d{2}", date):
            print("Некорректный формат даты!")
            return
        category = input("Введите категорию (Доход/Расход): ")
        # Проверка категории (должна быть "Доход" или "Расход")
        if category not in ["Доход", "Расход"]:
            print("Некорректная категория!")
            return
        amount = float(input("Введите сумму: "))
        # Проверка формата суммы (число с плавающей точкой)
        try:
            amount = float(amount)
        except ValueError:
            print("Некорректный формат суммы!")
            return
        description = input("Введите описание: ")
        with open(self.file_path, 'a') as file:
            file.write(f"{date},{category},{amount},{description}\n")
        print("Запись успешно добавлена!")

    def edit_record(self) -> None:  # изменить запись
        record_id = int(input("Введите номер записи, которую хотите изменить: "))
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
        if record_id < 1 or record_id > len(lines):
            print("Некорректный номер записи!")
            return
        new_date = input("Введите новую дату (ГГГГ-ММ-ДД): ")
        # Проверка формата даты (ГГГГ-ММ-ДД)
        if not re.match(r"\d{4}-\d{2}-\d{2}", new_date):
            print("Некорректный формат даты!")
            return
        new_category = input("Введите новую категорию (Доход/Расход): ")
        # Проверка категории (должна быть "Доход" или "Расход")
        if new_category not in ["Доход", "Расход"]:
            print("Некорректная категория!")
            return
        new_amount = float(input("Введите новую сумму: "))
        # Проверка формата суммы (число с плавающей точкой)
        try:
            new_amount = float(new_amount)
        except ValueError:
            print("Некорректный формат суммы!")
            return
        new_description = input("Введите новое описание: ")
        lines[record_id - 1] = f"{new_date},{new_category},{new_amount},{new_description}\n"
        with open(self.file_path, 'w') as file:
            file.writelines(lines)
        print("Запись успешно изменена!")

    def search_records(self) -> None:  # найти запись
        keyword = input("Введите ключевое слово для поиска: ")
        found_records = []
        with open(self.file_path, 'r') as file:
            for line in file:
                record = line.strip().split(',')
                if keyword.lower() in record[3].lower():
                    found_records.append(line)
        if len(found_records) != 0:
            print("Найденные записи:")
            for record in found_records:
                record = record.strip().split(',')
                print(f"{record[0]} {record[1]} {record[2]} {record[3]}")
        else:
            print("Записи не найдены.")

    def deleite_records(self) -> None:
        record_id = int(input("Введите номер записи, которую хотите удалить: "))
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
        if record_id < 1 or record_id > len(lines):
            print("Некорректный номер записи!")
            return
        # Удаляем соответствующую строку из списка
        del lines[record_id - 1]
        with open(self.file_path, 'w') as file:
            file.writelines(lines)
        print("Запись успешно удалена!")


def test_add_record():  # тест на добавление записи
    file_path = "test_expenses.txt"
    expense_tracker = ExpenseTracker(file_path)
    # Добавляем запись
    expense_tracker.add_record()
    with open(file_path, 'r') as file:
        lines = file.readlines()
        assert len(lines) != 0
    # Проверка содержимого добавленной записи
    record = lines[0].strip().split(',')
    assert record[0] == "2024-03-04"  # Проверяемая дата
    assert record[1] == "Расход"  # Проверяемая категория
    assert float(record[2]) == 5000.0  # Проверяемая сумма
    assert record[3] == "Покупка продуктов на др жены"  # Проверяемое описание


def test_edit_record():  # тест на изменение записи
    file_path = "test_expenses.txt"
    expense_tracker = ExpenseTracker(file_path)
    # Добавляем запись для редактирования
    expense_tracker.add_record()
    # Редактируем добавленную запись
    expense_tracker.edit_record()
    with open(file_path, 'r') as file:
        lines = file.readlines()
        assert len(lines) != 0
    # Проверка содержимого отредактированной записи
    record = lines[0].strip().split(',')
    assert record[0] == "2024-03-01"  # Проверяемая новая дата
    assert record[1] == "Доход"  # Проверяемая новая категория
    assert float(record[2]) == 45000.0  # Проверяемая новая сумма
    assert record[3] == "Зарплата"  # Проверяемое новое описание


def test_delete_record():
    file_path = "test_expenses.txt"
    expense_tracker = ExpenseTracker(file_path)
    # Добавляем запись для удаления
    expense_tracker.add_record()
    # Удаляем добавленную запись с индексом "1"
    expense_tracker.deleite_records()
    with open(file_path, 'r') as file:
        lines = file.readlines()
        assert len(lines) == 0


# основной блок
file_path: str = "expenses.txt"
expense_tracker: ExpenseTracker = ExpenseTracker(file_path)

while True:
    print(f"\n"
          f"1. Вывести баланс \n"
          f"2. Добавить запись\n"
          f"3. Редактировать запись\n"
          f"4. Поиск по записям")
    choice: str = input("Выберите действие: ")
    if choice == "1":
        expense_tracker.show_balance()
    elif choice == "2":
        expense_tracker.add_record()
    elif choice == "3":
        expense_tracker.edit_record()
    elif choice == "4":
        expense_tracker.search_records()
    elif choice == "5":
        expense_tracker.deleite_records()
    else:
        print("Некорректный выбор.")


# test_add_record()
# test_edit_record()
# test_delete_record()

class ExpenseTracker:
    def __init__(self, file_path):
        self.file_path = file_path

    def show_balance(self):
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

    def add_record(self):
        date = input("Введите дату (ГГГГ-ММ-ДД): ")
        category = input("Введите категорию (Доход/Расход): ")
        amount = float(input("Введите сумму: "))
        description = input("Введите описание: ")
        with open(self.file_path, 'a') as file:
            file.write(f"{date},{category},{amount},{description}\n")
        print("Запись успешно добавлена!")

    def edit_record(self):
        record_id = int(input("Введите номер записи, которую хотите изменить: "))
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
        if record_id < 1 or record_id > len(lines):
            print("Некорректный номер записи!")
            return
        new_date = input("Введите новую дату (ГГГГ-ММ-ДД): ")
        new_category = input("Введите новую категорию (Доход/Расход): ")
        new_amount = float(input("Введите новую сумму: "))
        new_description = input("Введите новое описание: ")
        lines[record_id - 1] = f"{new_date},{new_category},{new_amount},{new_description}\n"
        with open(self.file_path, 'w') as file:
            file.writelines(lines)
        print("Запись успешно изменена!")

    def search_records(self):
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


file_path = "expenses.txt"
expense_tracker = ExpenseTracker(file_path)

while True:
    print(f"\n1. Вывести баланс \n2. Добавить запись\n3. Редактировать запись\n4. Поиск по записям")
    choice = input("Выберите действие: ")
    if choice == "1":
        expense_tracker.show_balance()
    elif choice == "2":
        expense_tracker.add_record()
    elif choice == "3":
        expense_tracker.edit_record()
    elif choice == "4":
        expense_tracker.search_records()
    else:
        print("Некорректный выбор.")


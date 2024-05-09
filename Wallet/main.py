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
        pass

    def edit_record(self):
        pass

    def search_records(self):
        pass


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


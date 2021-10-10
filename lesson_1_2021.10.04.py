#1

name = input("Введите своё имя: ")
print("Здравствуй", name, "!", "Как поживаешь?")
h_a_y = input("Как поживаешь?")
print("Настолько", h_a_y, "?", "Хм, ну да ладно.", "А время не подскажешь?")
time = input("Подскажите время собеседнику: ")
print("Ха! Вот и неверно. Время осваивать новую профессию и научиться уже грамотно писать код ")

#2

enter_time = int(input("Введите время в секундах: "))
hours = enter_time // 3600
minutes = enter_time // 60 - hours * 60
seconds = enter_time % 60
convertions_time = (f"{hours:02}:{minutes:02}:{seconds:02}")
print(convertions_time)

#3

a = input("Введите число: ")

if a > '0':
    print(f"{a} + {a+a} + {a+a+a} = {int(a)+ int(a+a)+ int(a+a+a)}")
else:
    print("Неверное число")

#4

num_init = int(input("Введите целое положительное число: "))
max_num = 0
num = num_init
while num > 0:
    digit = num % 10
    if digit > max_num:
        max_num = digit
        if max_num == 9:
            break
    num = num // 10
print(f"Максимальная цифра в числе {num_init} - {max_num}")

#5

incomes = int(input("Введите ваши доходы: $"))
costs = int(input("Введите ваши расходы: $"))
gross_profit = incomes - costs
if gross_profit > 0:
    print(f"Ваша прибыль составляет {gross_profit} $")
    print(f"Ваша рентабельность составляет {gross_profit * 100 / incomes}%")
    work_squad = int(input("Введите численность вашего персонала: "))
    print(f"Прибыль для каждого отдельного сотрудника составит {gross_profit / work_squad} $")
elif gross_profit < 0:
    print(f"Ваш убыток составляет {gross_profit} $")
else:
    print(f"Ваша компания отработала в 'ноль' ")


#6

#Даже просмотрев решение перед началом новой темы, я не до конца разобрался с задачей...

first_day = float(input("Введите результат в первый день:  км"))
last_day = float(input("Введите результат в последний день: км"))
stage = 1
while first_day < 0 and last_day < 0:
    break
elif first_day < last_day:
    first_day= first_day * 0.1
    stage = stage + 1
    print(f"Бегун выполнит результат за {stage} дней")
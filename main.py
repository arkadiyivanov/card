# Создайте приложение, которое проверяет правильность номера
# введенной кредитной карты (см. алгоритм Луна
numbers_card = 123456789

# int(input("Введите номер банковской карты"))
card = 123456789

list_ = list(str(numbers_card))
list2 = list(map(int, list_))

sum_even = 0
sum_odd = 0

a = 0

for num_ in list2[::-1]:
    if num_ % 2 == 1:
        sum_odd += num_
    if num_ % 2 == 0:
        a = num_ * 2
        sum_even += a
sum_control = sum_odd + sum_even
if sum_control > 9:
    sum_control -= 9
print(sum_control)

list2.append(0)


print(list2)
print(sum_odd)
print(sum_even)


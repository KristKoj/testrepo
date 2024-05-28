len1 = float(input("Введите первую длину в метрах: "))
len2 = float(input("Введите вторую длину в футах: "))

len2 = len2 * 0.3048

if len1 < len2:
    print("Первая длина меньше второй")
elif len2 < len1:
    print("Вторая длина меньше первой")
else:
    print("Длины равны")


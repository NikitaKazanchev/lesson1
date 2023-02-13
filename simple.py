a = 2
b = 0.5
print(a+b)

name = 'Nikita'
print(f'Привет, {name}!')

v = int(input('Введите число от 1 до 10: '))
print(v+10)

name = input('Введите ваше имя: ')
print(f'Привет, {name}! Как дела?')

print(type(float('1')))
print(type(int('2.5')))
print(type(bool(1)))
print(type(bool("")))
print(type(bool(0)))

list1 = [3, 5, 7, 9, 10.5]
print(list1)
list1.append('Python')
print(len(list1))
print(list1[0])
print(list1[-1])
print(list1[1:4])
list1.remove('Python')

weather = {"city": "Москва", "temperature": "20"}
print(weather["city"])
weather["temperature"] = "5"
print(weather)
print(weather.get("country"))
print(weather.get("country", "Россия"))
weather['date'] = "27.05.2019"
print(len(weather))
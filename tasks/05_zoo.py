
# есть список животных в зоопарке
zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# lion на позиции 0, kangaroo на позиции 1.
# Значит, чтобы вставить bear между ними, вставляем по индексу 1
zoo.insert(1, 'bear')
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
zoo.extend(birds)
print(zoo)

# уберите слона
zoo.remove('elephant')
print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
print('Лев сидит в клетке номер', zoo.index('lion') + 1)
print('Жаворонок сидит в клетке номер', zoo.index('lark') + 1)
import random

def find_numbers():
  try:
    # Вариант со случайной генерацией количества элементов списков
    # ar_1 = [random.randint(1,20) for _ in range(random.randint(1,20))]
    # ar_2 = [random.randint(1,20) for _ in range(random.randint(1,20))]

    # Вариант с ручным вводом количества элементов списков
    ar_1 = [random.randint(1,20) for _ in range(int(input('Введите количество чисел первого списка: ')))]
    ar_2 = [random.randint(1,20) for _ in range(int(input('Введите количество чисел второго списка: ')))]
    print(f'Список 1:\n{ar_1}')
    print(f'Список 2:\n{ar_2}')
    result = set(ar_1) & set(ar_2)
    if len(result) == 0:
      print(f"Уникальные числа входящие в оба списка, не найдены,\nСписки {ar_1} и {ar_2} - не пересекаются")
    else:
      print(f'{result} - уникальные числа, входящие в оба списка.')
  except:
    return 'Неверный формат ввода данных!'
  
find_numbers()

import random

def berries():
  # Генерируем случайное количество кустов
  numbs = random.randint(10, 30)
  # Генерируем случайное количество ягод на каждом кусте
  bush = [random.randint(1,50) for _ in range(numbs)]
  print(f'Количество кустов = {numbs}')
  print(f'Исходные данные количества ягод на кашдом кусте:\n{bush}')
  max_quantity = 0
  #Определяем максимальное число ягод за один проход
  for i in range(numbs):
    quantity = bush[i] + bush[(i+1) % numbs] + bush[(i+2) % numbs]
    max_quantity = max(max_quantity, quantity)
  print(f'Максимальное количество ягод собранное за один проход = {quantity}')
   
berries()

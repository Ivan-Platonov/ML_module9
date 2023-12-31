print('Задача 6. Коровы')

# Для коров есть 10 стойл. В каждом из них условия для животных разные, поэтому и молока они дают по-разному. В первом стойле производят 2 литра в день, во втором — 4, в третьем — 6, далее — 8, 10, 12, 14, 16, 18 и 20. При этом коровы находятся не во всех стойлах. Свободные и занятые обозначаются строкой из букв a и b, где a — свободное стойло, b — занятое.

# Что нужно сделать

# Напишите программу для подсчёта получаемого молока в коровнике. Важно учитывать следующее взаимодействие: пользователь вводит строку из десяти символов a и b. Необходимо определить, сколько в итоге будет произведено молока за день.


stalls = input('Введите занятость стойл (строка из 10 символов a и b): ')
milk_sum = 0

for count, stall in enumerate(stalls):
  if stall == 'b':
    milk_sum += (count + 1) * 2

print('\nПроизведено молока за день:', milk_sum)
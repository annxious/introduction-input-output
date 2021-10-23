# Напишите программу, которая считывает три строки по очереди, а затем выводит их в той же последовательности, каждую на отдельной строчке. 
# Формат входных данных На вход программе подаются три строки, каждая на отдельной строке.
# Формат выходных данных. Программа должна вывести введенные строки в той же последовательности, каждую на отдельной строке.
# Sample Input 1:
# I was
# born
# this way
# Sample Output 1:
# I was
# born
# this way

# My solution
words = input()
print (words)
words = input()
print (words)
words = input()
print (words)

# Interestin solution
print(input(), input(), input(), sep = '\n')

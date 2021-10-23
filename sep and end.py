#Напишите программу, которая считывает строку-разделитель и три строки, а затем выводит указанные строки через разделитель.
#Формат входных данных
#На вход программе подаётся строка-разделитель и три строки, каждая на отдельной строке.
#Формат выходных данных
#Программа должна вывести введённые три строки через разделитель.
#Тестовые данные
#Sample Input 1:
#*
#Раз
#Два
#Три
#Sample Output 1:
#Раз*Два*Три
#Sample Input 3:
#python
#1
#2
#3
#Sample Output 3:
#1python2python3

# My solution
sepa=input()
word1=input()
word2=input()
word3=input()
print(word1, word2, word3, sep=sepa)

# Interesting solution
a, b, c, d = input(), input(), input(), input()
print(b, c, d, sep=a)

#Найдите количество цифр в записи числа 100! (факториал от 100).

def fact(n):
   if n == 1:
       return 1
   return n * fact(n-1)


print(fact(100))
a = fact(100)
print(len(str(a)))



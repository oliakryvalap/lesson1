#Требуется определить, можно ли от шоколадки размером n × m долек отломить 
#k долек, если разрешается сделать один разлом по прямой между дольками 
#(то есть разломить шоколадку на два прямоугольника).

#*Пример:*

#3 2 4 -> no
#3 2 1 -> yes
n = int (input('Введите количество долек вдоль: '))
m = int (input('Введите количество долек поперек: '))
k = int (input ("Введите количество долек, которых нужно надломить")) 

if n%k == 0 or m%k == 0:
      print('Yes')
else: print('No')





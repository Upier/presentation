'''
3. 합계를 구하는 함수 작성 : my_sum()
4. 평균을 구하는 함수 작성 : my_avg()
'''

def my_sum(number1, number2):
  sum = number1 + number2
  return sum

def my_avg(number1,number2):
    avg = (number1+number2)/2
    return avg


number1 = int(input('number1 : '))
number2 = int(input('number2 : '))

print('sum:{0:3}'.format(my_sum(number1, number2)))
print('avg:{0:3.2f}'.format(my_avg(number1, number2)))


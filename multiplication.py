num1 = int(input('請輸入數字1:'))
num2 = int(input('請輸入數字2:'))
symb = input('請輸入運算符號:')

if symb == '*':
    print( num1, '*',  num2, '=', num1*num2)
elif symb == '/':
    print(num1, '/',  num2, '=', num1/num2)
elif symb == '+':
    print(num1, '+',  num2, '=', num1+num2)
elif symb == '-':
    print(num1, '-',  num2, '=', num1-num2)
else:
    break
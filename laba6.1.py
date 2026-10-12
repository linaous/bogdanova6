
def f(s):
    s=s.lower()
    v='aeiouy'
    a=0
    b=0

    for c in s:
        if c.isalpha():
            if c in v:
                a+=1
            else:
                b+=1
    return a, b 
t= input('Введите строку:')
x,y=f(t)
print(f'Гласных:{x}, Согласных:{y}')


        



















def func():
    a = int(input("Wpisz pierwszą liczbę: "))
    b = int(input("Wpisz drugą liczbę: "))
    c = int(input("Wpisz trzecią liczbę: "))
    d = int(input("Wpisz czwartą liczbę: "))

    if a>b:
        print((a+b+c+d)/4)
    else:
        print("Błąd")

# func()

def func1():
    a = []
    sr = 0
    for i in range(4):
        i = int(input(f'Wpisz {i+1} liczbę: '))
        a.append(i)

    if a[0]>a[1]:
        for i in a:
            sr+=i
        sr=sr/len(a)
        print(sr)
        sr = 0
    else:
        print("Błąd")

func1()
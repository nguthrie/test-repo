

def less_than_n(n):
    n1 = 0 
    n2 = 1
    while n2 < n:
        print(n1)
        temp = n1
        n1 = n2
        n2 = n2 + temp

less_than_n(1000)
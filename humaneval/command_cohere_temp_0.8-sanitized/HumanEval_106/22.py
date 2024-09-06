def f(n):
    list_man = []
    for i in range(1, n+1):
        if i % 2 == 0:
            list_man.append(factorial(i))
        else:
            list_man.append(sum(range(1, i+1)))
    return list_man
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
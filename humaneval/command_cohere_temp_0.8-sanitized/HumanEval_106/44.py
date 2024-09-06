def f(n):
    l = []
    for i in range(1, n+1):
        if i % 2 == 0:
            l.append(factorial(i))
        else:
            l.append(sum(range(1, i+1)))
    return l
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
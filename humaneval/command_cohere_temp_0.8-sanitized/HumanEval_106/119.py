def f(n):
    ls = []
    for i in range(1, n+1):
        if i % 2 == 0:
            ls.append(factorial(i))
        else:
            ls.append(sum(range(1, i+1)))
    return ls
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
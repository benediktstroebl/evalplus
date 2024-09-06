def f(n):
    r = []
    for i in range(1, n+1):
        if i % 2 == 0:
            r.append(factorial(i))
        else:
            r.append(sum(range(1, i+1)))
    return r
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
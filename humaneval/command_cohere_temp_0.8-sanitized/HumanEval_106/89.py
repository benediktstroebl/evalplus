def f(n):
    out = []
    for i in range(1, n+1):
        if i % 2 == 0:
            out.append(factorial(i))
        else:
            out.append(sum(range(1, i+1)))
    return out
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
def f(n):
    li = []
    for i in range(1, n+1):
        if i % 2 == 0:
            li.append(factorial(i))
        else:
            li.append(sum(range(1, i+1)))
    return li
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
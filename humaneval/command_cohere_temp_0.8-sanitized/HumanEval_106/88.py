def f(n):
    list_ = []
    for i in range(1, n+1):
        if i % 2 == 0:
            list_.append(factorial(i))
        else:
            list_.append(sum(range(1, i+1)))
    return list_
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
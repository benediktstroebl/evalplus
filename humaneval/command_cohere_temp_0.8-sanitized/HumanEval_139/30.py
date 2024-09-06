def special_factorial(n):
    factorial_sum = 1
    for i in range(2, n + 1):
        factorial_sum *= i
    return factorial_sum
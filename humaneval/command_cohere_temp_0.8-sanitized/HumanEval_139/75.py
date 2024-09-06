def special_factorial(n):
    factorial_sequence = [1]
    for i in range(2, n+1):
        factorial_sequence.append(factorial_sequence[i-1] * i)
    return factorial_sequence[n]
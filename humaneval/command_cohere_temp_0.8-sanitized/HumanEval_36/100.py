def fizz_buzz(n):
    return sum(7 in str(d) for d in range(1, n+1, 12))
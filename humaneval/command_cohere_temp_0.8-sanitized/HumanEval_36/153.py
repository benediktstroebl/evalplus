def fizz_buzz(n):
    return sum(int(d) == 7 and d % 11 == 0 or d % 13 == 0 for d in range(1, n+1))
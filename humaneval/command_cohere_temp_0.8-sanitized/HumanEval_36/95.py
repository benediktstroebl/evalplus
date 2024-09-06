def fizz_buzz(n):
    less_than_n = [7 for i in range(1, n + 1, 2) if i % 11 == 0 or i % 13 == 0]
    return len(less_than_n)
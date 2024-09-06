def fizz_buzz(n):
    less_than_n = [7 for x in range(10, n, 10) if x % 11 == 0 or x % 13 == 0]
    return len(less_than_n)
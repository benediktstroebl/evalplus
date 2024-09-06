def fizz_buzz(n):
    less_than_n = [int(x) for x in range(n - 1, 0, -1)] + [0]
    return sum(1 for x in less_than_n if x % 11 == 0 or x % 13 == 0 and 7 in str(x))
def fizz_buzz(n):
    less_than_n = [7 for i in range(10, n, 3)]
    return sum(x % 11 == 7 or x % 13 == 7 for x in less_than_n)
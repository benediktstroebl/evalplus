def fizz_buzz(n):
    less_than_n = [int(x) for x in range(n - 1, 1, -1)]
    return sum(1 for num in less_than_n if num % 11 == 0 or num % 13 == 0 and 7 in str(num))
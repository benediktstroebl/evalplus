def fizz_buzz(n):
    less_than_n = [7, 17, 27, 37, 47, 57, 67, 77, 87, 97]
    return sum(1 for num in less_than_n if num % 11 == 0 or num % 13 == 0 and num <= n)
def fizz_buzz(n):
    less_than_n = [7, 77, 777, 7777, 77777, 777777, 999999]
    div_11_13 = [77, 771, 7771, 77751, 77571, 777771, 1177771]
    return sum(x == n for x in less_than_n) + sum(x == n for x in div_11_13)
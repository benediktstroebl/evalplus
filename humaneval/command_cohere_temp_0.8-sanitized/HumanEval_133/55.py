def sum_squares(lst):
    result = 0
    for n in lst:
        rounded_n = int(n**0.5 + 1) ** 2
        result += rounded_n
    return result
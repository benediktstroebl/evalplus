def sum_squares(lst):
    result = sum(x ** 2 for x in lst if x % 1 == 0)
    return result
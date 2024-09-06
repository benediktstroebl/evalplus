def double_the_difference(lst):
    odd_squares = sum(x ** 2 for x in lst if x % 2 and x >= 0 and isinstance(x, int))
    return 0 if not lst else odd_squares
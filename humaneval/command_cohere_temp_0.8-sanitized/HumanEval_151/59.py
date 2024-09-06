def double_the_difference(lst):
    odd_squares = sum(x**2 for x in lst if x % 2 and x >= 0 and isinstance(x, int))
    return int(odd_squares)
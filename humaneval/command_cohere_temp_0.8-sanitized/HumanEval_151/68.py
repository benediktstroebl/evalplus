def double_the_difference(lst):
    odd_squares = sum(x**2 for x in lst if x % 2 and x >= 0)
    return int(odd_squares)
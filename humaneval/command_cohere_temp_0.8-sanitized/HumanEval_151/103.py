def double_the_difference(lst):
    odd_squares = [x**2 for x in lst if x % 2 == 1 and x >= 0]
    return sum(odd_squares) if odd_squares else 0
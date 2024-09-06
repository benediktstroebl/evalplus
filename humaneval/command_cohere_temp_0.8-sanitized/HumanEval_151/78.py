def double_the_difference(lst):
    odd_sqrs = sum(x**2 for x in lst if x % 2 and x >= 0)
    return 0 if not lst else odd_sqrs
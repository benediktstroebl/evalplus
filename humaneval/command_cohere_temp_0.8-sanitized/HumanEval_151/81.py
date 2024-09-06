def double_the_difference(lst):
    odd_sq = sum(x**2 for x in lst if x % 2 != 0 and x >= 0)
    return int(odd_sq)
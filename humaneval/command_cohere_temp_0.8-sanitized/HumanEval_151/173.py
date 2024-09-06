def double_the_difference(lst):
    odd = [x for x in lst if x % 2 != 0 and x >= 0]
    return sum(x * x for x in odd)
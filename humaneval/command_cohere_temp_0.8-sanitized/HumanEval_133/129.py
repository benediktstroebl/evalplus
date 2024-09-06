def sum_squares(lst):
    result = sum(int(round(x)**2 for x in lst if x > 0))
    if not result:
        return 0
    return result
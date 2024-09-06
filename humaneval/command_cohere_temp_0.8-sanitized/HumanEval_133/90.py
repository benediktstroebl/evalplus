def sum_squares(lst):
    result = sum(int(round(x)**2 for x in lst if x > 0))
    if not lst or not isinstance(result, int):
        return result
    return result + sum(int(x)**2 for x in lst if x < 1)
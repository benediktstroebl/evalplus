def sum_squares(lst):
    result = 0
    for n in lst:
        if isinstance(n, float):
            n = n ** 2
        elif n < 0:
            n = -n
        result += n

    return result
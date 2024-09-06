def double_the_difference(lst):
    result = 0
    for n in lst:
        if isinstance(n, int) and n > 0:
            result += n**2
    return result
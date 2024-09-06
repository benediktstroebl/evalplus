def sum_squares(lst):
    result = 0
    for n in lst:
        result += n**2
    return int(result)
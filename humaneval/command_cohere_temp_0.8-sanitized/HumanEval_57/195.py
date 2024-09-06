def monotonic(lst):
    if len(lst) < 2:
        return True
    a = lst[0]
    b = lst[1]
    # check if the list is either monotonically increasing or decreasing
    for c in lst[2:]:
        if a > b > c or a < b < c:
            return False
        a, b = b, c
    return True
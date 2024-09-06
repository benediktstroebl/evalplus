def monotonic(lst):
    if len(lst) < 2:
        return True
    a = lst[0]
    b = lst[1]
    # Check if the list is either monotonically increasing or decreasing
    return (a <= b) == (b <= lst[2])
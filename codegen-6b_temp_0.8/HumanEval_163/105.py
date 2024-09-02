
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    range_start = abs(a)
    range_end = abs(b)
    result = []
    if range_start < 10:
        result = [range_start]
    elif range_start > 10:
        result = [int(str(range_start)[0])]
    if range_end < 10:
        result = result + [range_end]
    elif range_end > 10:
        result = result + [int(str(range_end)[-1])]
    return result


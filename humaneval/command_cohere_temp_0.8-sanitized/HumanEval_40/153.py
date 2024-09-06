def triples_sum_to_zero(l: list):
    """
    Returns True if three distinct elements in the list sum up to zero, False - otherwise.
    """
    seen = set()
    for i in l:
        if 0 == i:
            continue
        x, y = -i, i
        do_sum = False
        while x != 0:
            if x in seen and y in seen:
                return True
            seen.add(x)
            seen.add(y)
            if x > 0:
                do_sum = not do_sum
            x = x * do_sum - y
        y = -x
    return False
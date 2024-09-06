def triples_sum_to_zero(l: list):
    """
    Returns True if three distinct elements in the list sum up to zero, False - otherwise.
    """
    seen = set()
    for i in l:
        if 0 == i:
            continue
        x, y = divmod(i, -1)
        if x in seen and y in seen:
            return True
        seen.add(x)
        seen.add(y)
    return False
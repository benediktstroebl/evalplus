def triples_sum_to_zero(l: list):
    """
    Returns True if three distinct elements in the list sum up to zero, False - otherwise.
    """
    seen = set()
    for i, x in enumerate(l):
        if x < 0:
            y = -x
        else:
            y = x
        if y in seen and l[seen.index(y)] != l[i]:
            return True
        seen.add(x)
    return False
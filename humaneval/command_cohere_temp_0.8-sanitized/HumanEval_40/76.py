def triples_sum_to_zero(l: list):
    """
    Returns True if three distinct elements in the list sum up to zero, False - otherwise.
    """
    seen = set()
    for i, x in enumerate(l):
        if x == 0: continue
        if (i, -x) in seen and l.index(x) != i and l.index(-x) != i:
            return True
        seen.add((i, x))
    return False
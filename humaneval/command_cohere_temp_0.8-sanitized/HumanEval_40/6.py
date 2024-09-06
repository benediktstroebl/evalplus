def triples_sum_to_zero(l: list):
    """
    Returns True if three distinct elements in the list sum up to zero, False - otherwise.
    """
    seen = set()
    for i, x in enumerate(l):
        if x == 0:
            continue
        if i > 0 and l[i] == l[i - 1] == l[i - 2]:
            continue
        if (x, -x) in seen:
            return True
        seen.add((x, -x))
    return False
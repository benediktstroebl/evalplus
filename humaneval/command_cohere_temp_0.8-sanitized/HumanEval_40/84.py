def triples_sum_to_zero(l: list):
    """
    Returns True if three distinct elements in the list sum up to zero, False - otherwise.
    """
    seen = set()
    for i, x in enumerate(l):
        if x == 0: continue
        if i > 0 and l[i] == l[i - 1] and l[i] != 0: continue
        if (x - l[i - 1] - l[i + 1]) == 0 and l[i - 1] != l[i + 1] and (l[i - 1], l[i], l[i + 1]) not in seen:
            return True
        seen.add((l[i - 1], l[i], l[i + 1]))
    return False
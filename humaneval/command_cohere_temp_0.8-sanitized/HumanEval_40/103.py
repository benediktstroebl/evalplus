def triples_sum_to_zero(l: list):
    """
    Returns True if three distinct elements in the list sum up to zero, False - otherwise.
    """
    seen = set()
    for i, x in enumerate(l):
        if x == 0: continue
        if i > 0 and l[i] == l[i - 1] and l[i] != 0: continue
        if x == -l[i] and l[i] != 0: return True
        for j in range(i + 1, len(l)):
            y = l[j]
            if x + y == -l[j] and x != 0 and y != 0 and (x, y) not in seen:
                seen.add((x, y))
                if triples_sum_to_zero(l, x, y, j): return True
    return False
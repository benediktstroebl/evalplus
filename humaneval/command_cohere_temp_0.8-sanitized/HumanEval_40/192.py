def triples_sum_to_zero(l: list):
    """
    Returns True if three distinct elements in the list sum up to zero, False - otherwise.
    """
    seen = set()
    for i, x in enumerate(l):
        if x == 0:
            continue
        y_found, z_found = False, False
        for j, y in enumerate(l[i + 1:]):
            if y == 0:
                continue
            if x + y + l[j + 1] == 0 and x != y and j != i:
                y_found = True
                z_found = True
                break
        if y_found and z_found and (i, x, y) not in seen:
            return True
        seen.add((i, x, y))
    return False
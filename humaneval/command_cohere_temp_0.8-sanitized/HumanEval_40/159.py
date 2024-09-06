def triples_sum_to_zero(l: list):
    """
    Returns True if three distinct elements in the list sum up to zero, False - otherwise.
    """
    seen = set()
    for i, x in enumerate(l):
        if x < 0:
            for j, y in enumerate(l[i+1:]):
                if y < 0 and x + y == 0 and i != j and (i, x, y) not in seen:
                    seen.add((i, x, y))
                    z = -x - y
                    if z > 0 and (z, i, x, y) not in seen:
                        return True
                    else:
                        return False
        elif l[i+1:] and l[i+1:] != [x]:
            return triples_sum_to_zero(l[i+1:])
    return False
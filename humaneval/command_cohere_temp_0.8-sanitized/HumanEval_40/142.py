def triples_sum_to_zero(l: list):
    """
    Returns True if three distinct elements in the list sum up to zero, False - otherwise.
    """
    seen = set()
    for i, x in enumerate(l):
        if x < 0:
            for j, y in enumerate(l[i+1:]):
                if y < 0 and x + y == 0 and i != j:
                    if i < j and (i, j) not in seen:
                        seen.add((i, j))
                    elif j < i and (j, i) not in seen:
                        seen.add((j, i))
                    else:
                        return False
                    if len(seen) > 2:
                        return False
                else:
                    return False
            return False
        else:
            for j, y in enumerate(l[i+1:]):
                if x + y == 0 and i != j:
                    if i < j and (i, j) not in seen:
                        seen.add((i, j))
                    elif j < i and (j, i) not in seen:
                        seen.add((j, i))
                    else:
                        return False
                    if len(seen) > 2:
                        return False
                else:
                    return False
            return False
    return False
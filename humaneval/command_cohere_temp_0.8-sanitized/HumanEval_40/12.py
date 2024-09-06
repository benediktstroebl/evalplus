def triples_sum_to_zero(l: list):
    """
    Returns True if three distinct elements in the list sum up to zero, False - otherwise.
    """
    seen = set()
    for i, x in enumerate(l):
        if x < 0:
            for j, y in enumerate(l[i+1:]):
                if y < 0 and x + y == 0 and i != j:
                    if i < j:
                        return True
                    elif j < i:
                        return True
                    else:
                        return False
                elif y > 0 and x + y == 0 and i != j and j in seen:
                    return True
                seen.add(j)
    return False
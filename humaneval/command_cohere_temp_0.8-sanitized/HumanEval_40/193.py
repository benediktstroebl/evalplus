def triples_sum_to_zero(l: list):
    """
    Returns True if three distinct elements in the list sum up to zero, False - otherwise.
    """
    seen = set()
    for i, x in enumerate(l):
        if x < 0:
            for j, y in enumerate(l[i+1:]):
                if y < 0 and x + y > 0 and (i, j) not in seen:
                    if l[j+1] > 0 and (x + y + l[j+1]) == 0:
                        return True
                        seen.add((i, j))
                    elif l[j+1] < 0 and (x + y - l[j+1]) == 0:
                        return True
                        seen.add((i, j))
    return False
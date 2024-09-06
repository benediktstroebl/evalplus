def triples_sum_to_zero(l: list):
    """
    Returns True if three distinct elements in the list sum up to zero, False - otherwise.
    """
    seen = set()
    for i, x in enumerate(l):
        if x < 0:
            for j, y in enumerate(l[i+1:]):
                if y < 0 and x + y > 0 and j != i + 1 and (i, x, y) not in seen:
                    seen.add((i, x, y))
                    if l[k] > 0 and x + y + l[k] == 0 and k != i and k != j:
                        return True
                        break
                elif y > 0 and x + y < 0 and j != i + 1 and (i, x, y) not in seen:
                    seen.add((i, x, y))
                    if l[k] < 0 and x + y + l[k] == 0 and k != i and k != j:
                        return True
                        break
        elif x > 0:
            for j, y in enumerate(l[i+1:]):
                if x + y < 0 and j != i + 1 and (i, x, y) not in seen:
                    seen.add((i, x, y))
                    if l[k] < 0 and x + y + l[k] == 0 and k != i and k != j:
                        return True
                        break
                elif y < 0 and x + y > 0 and j != i + 1 and (i, x, y) not in seen:
                    seen.add((i, x, y))
                    if l[k] > 0 and x + y + l[k] == 0 and k != i and k != j:
                        return True
                        break
    return False
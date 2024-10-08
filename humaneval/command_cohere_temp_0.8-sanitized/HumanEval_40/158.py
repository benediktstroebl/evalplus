def triples_sum_to_zero(l: list):
    """
    Returns True if three distinct elements in the list sum up to zero, False - otherwise.
    """
    seen = set()
    for i, x in enumerate(l):
        if x < 0:
            for j, y in enumerate(l[i+1:]):
                if y < 0 and x + y > 0 and j != i + 1 and (j, x, y) not in seen:
                    seen.add((j, x, y))
                    if l[k] > 0 and j != k and k != i and (x, y, l[k]) not in seen:
                        return True
                        seen.add((x, y, l[k]))
                        break
                if j == len(l) - 1:
                    break
            i += 1
        elif l[-1] > 0:
            for j, y in enumerate(reversed(l[:i])):
                if y > 0 and x + y < 0 and j != i + 1 and (y, x, j) not in seen:
                    seen.add((y, x, j))
                    if l[k] < 0 and j != k and k != i and (j, l[k], x) not in seen:
                        return True
                        seen.add((j, l[k], x))
                        break
                if j == i:
                    break
            i = len(l) - 1
        if i == len(l) - 1:
            return False
    return False
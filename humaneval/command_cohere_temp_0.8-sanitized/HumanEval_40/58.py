def triples_sum_to_zero(l: list):
    """
    Returns True if three distinct elements in the list sum up to zero, False - otherwise.
    """
    seen = set()
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if len(set([l[i], l[j], l[k]])) == 3 and sum( [l[i], l[j], l[k]]) == 0:
                    return True
                if l[i] == l[j] or l[j] == l[k] or l[i] == l[k]:
                    continue
                else:
                    seen.add(l[i])
                    seen.add(l[j])
                    seen.add(l[k])
                    if len(seen) == 3 and sum(seen) == 0:
                        return True
    return False
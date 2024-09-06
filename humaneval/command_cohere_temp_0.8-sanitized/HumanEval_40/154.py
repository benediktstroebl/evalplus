def triples_sum_to_zero(l: list):
    """
    Returns True if three distinct elements in the list sum up to zero, False - otherwise.
    """
    seen = set()
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if len(set([l[i], l[j], l[k]])) == 3 and l[i] + l[j] + l[k] == 0:
                    return True
                if l[i] + l[j] + l[k] in seen:
                    return False 
        seen.add(l[i])
    return False
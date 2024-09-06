def triples_sum_to_zero(l: list):
    """
    Returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    seen = set()
    for i in range(len(l)-2):
        for j in range(i+1, len(l)-1):
            for k in range(j+1, len(l)):
                if l[i] + l[j] + l[k] == 0 and i != j and j != k and (i, j, k) not in seen:
                    return True
        seen.add((i, j, l[i] + l[j]))
    return False
def triples_sum_to_zero(l: list):
    """
    Returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    seen = set()
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0 and i != j != k:
                    if {i, j, k} == seen:
                        return True
                    else:
                        seen.add({i, j, k})
    return False
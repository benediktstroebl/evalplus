def triples_sum_to_zero(l: list):
    """
    Returns True if there are three distinct elements in the list that sum to zero, and False otherwise.
    """
    seen = set()
    for a in l:
        if a == 0:
            continue
        if len(seen) == 2 and sum(seen) == -a:
            return True
        seen.add(a)
    return False
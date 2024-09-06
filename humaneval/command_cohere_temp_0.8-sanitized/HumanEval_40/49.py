def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    seen = set()
    for a in l:
        if a == 0:
            continue
        if len(seen) == 2:
            if a + seen.pop() + seen.pop() == 0:
                return True
        else:
            seen.add(a)
    return False
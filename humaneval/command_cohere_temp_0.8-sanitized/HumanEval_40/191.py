def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    seen = set()
    for a in l:
        if a > 0:
            if not seen and a:
                seen.add(a)
                continue
            if not seen or not seen.difference_update(lambda x: x == a - 1 or x == -a or x == 1):
                return False
        else:
            if not seen and a:
                continue
            if not seen or not seen.add(-a):
                return False
    return True
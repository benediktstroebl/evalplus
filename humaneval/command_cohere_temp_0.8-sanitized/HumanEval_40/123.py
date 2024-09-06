def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    seen = set()
    for a in l:
        if a < 0:
            continue
        for b in l:
            if b < 0 or a == b or (a, b) in seen:
                continue
            for c in l:
                if c < 0 or b == c or a + b + c != 0 or (b, c) in seen or (c, a) in seen:
                    continue
                else:
                    return True
                seen.add((a, b, c))
    return False
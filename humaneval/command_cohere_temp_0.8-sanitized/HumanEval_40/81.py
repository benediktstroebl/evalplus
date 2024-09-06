def triples_sum_to_zero(l: list):
    """
    Returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    seen = set()
    for a in l:
        if a == 0:
            continue
        for b in l:
            if a + b == 0 and (a, b) not in seen:
                seen.add((a, b))
                c = l[0] if a == l[0] + b else l[1] if a == l[1] + b else None
                if c is not None and (c, a, b) not in seen and not (c, b, a) in seen:
                    return True
                seen.remove((a, b))
    return False
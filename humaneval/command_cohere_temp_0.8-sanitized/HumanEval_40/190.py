def triples_sum_to_zero(l: list):
    seen = set()
    for a in l:
        for b in l:
            if a != b and a + b in seen:
                return True
            seen.add(a)
    return False
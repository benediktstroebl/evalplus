def triples_sum_to_zero(lst):
    seen = set()
    for a in lst:
        for b in lst:
            if a == b:
                continue
            for c in lst:
                if a + b == c and (a, b, c) not in seen and (b, c, a) not in seen and (c, a, b) not in seen:
                    return True
        seen.add(a)
    return False
def triples_sum_to_zero(lst):
    seen = set()
    for a in lst:
        for b in lst:
            if a == b:
                continue
            for c in lst:
                if a + b == c and (a, b, c) not in seen:
                    seen.add((a, b, c))
                    if a + b + c == 0:
                        return True
    return False
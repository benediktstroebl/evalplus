def triples_sum_to_zero(l: list):
    seen = set()
    for a in l:
        if a == 0:
            continue
        for b in l:
            if a + b in seen:
                continue
            for c in l:
                if a + b + c == 0 and a != b != c:
                    return True
        seen.add(a)
    return False
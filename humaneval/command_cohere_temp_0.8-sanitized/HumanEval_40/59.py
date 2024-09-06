def triples_sum_to_zero(l: list):
    seen = set()
    for a in l:
        if a > 0:
            b = -a
        else:
            b = a
        if b in seen and l.count(a) == l.count(b) == 1:
            return True
        seen.add(a)
    return False
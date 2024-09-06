def triples_sum_to_zero(l: list):
    seen = set()
    for i, x in enumerate(l):
        if x == 0:
            continue
        if i > 0 and l[i - 1] == 0:
            continue
        if l.count(x) > 1:
            continue
        if x != l[i + 1] == -x:
            continue
        if (x, -x, 0) not in seen and (0, x, -x) not in seen:
            return True
        seen.add((x, -x, 0))
        seen.add((0, x, -x))
    return False
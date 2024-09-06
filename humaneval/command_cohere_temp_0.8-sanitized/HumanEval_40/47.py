def triples_sum_to_zero(l: list):
    seen = set()
    for i, x in enumerate(l):
        if not seen:
            continue
        for j, y in enumerate(l[i+1:], i+1):
            if not seen | {x, y}:
                z = l[j+1:][x == y == 0]
                if z:
                    return True
            seen.add(j)
    return False
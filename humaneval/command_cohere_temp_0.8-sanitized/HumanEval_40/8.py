def triples_sum_to_zero(l: list):
    seen = set()
    for i, x in enumerate(l):
        if not seen:
            continue
        for j, y in enumerate(l[i+1:], i+1):
            if not seen | {x, y}:
                z = sum([x, y, l[j+1]])
                if not z: return True
            seen.add(y)
    return False
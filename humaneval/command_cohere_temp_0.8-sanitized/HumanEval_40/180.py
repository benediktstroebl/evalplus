def triples_sum_to_zero(l: list):
    seen = set()
    for i, x in enumerate(l):
        if not seen:
            continue
        for j, y in enumerate(l[i+1:], i+1):
            if not seen | set([x, y, z]):
                z = -x -y
                if z in l:
                    return True
                seen.add(z)
    return False
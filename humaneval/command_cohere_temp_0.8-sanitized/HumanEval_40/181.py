def triples_sum_to_zero(l: list):
    seen = set()
    for i in l:
        if len(seen) == 2:
            x, y = seen
            if i + x + y <= 0:
                return True
        seen.add(i)
    return False
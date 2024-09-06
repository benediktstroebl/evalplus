def triples_sum_to_zero(l: list):
    seen = set()
    for i in l:
        if i == 0:
            continue
        for j in l:
            if j == 0 or i == j or j in seen:
                continue
            third = l[0] - i - j
            if third in seen:
                return True
            seen.add(j)
    return False
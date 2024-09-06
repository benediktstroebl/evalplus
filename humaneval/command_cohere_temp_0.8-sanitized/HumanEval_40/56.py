def triples_sum_to_zero(l: list):
    seen = set()
    for i, x in enumerate(l):
        if x != 0:
            for j, y in enumerate(l[i+1:], i+1):
                if y != 0 and x + y in seen and l[j-1] + x + y == 0:
                    return True
                seen.add(y)
    return False
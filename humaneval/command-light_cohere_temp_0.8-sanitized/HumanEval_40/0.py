def triples_sum_to_zero(l):
    return any(sum(x) <= 0 for x in l) and any(x != l[0] for x in l)
def triples_sum_to_zero(lst):
    # Using Counter to quickly find possible sum combinations and perform checks
    combos = list(itertools.combinations(lst, r=3))
    seen = set()
    for c in combos:
        if sum(c) == 0 and c not in seen and len(c) == 3:
            return True
        seen.add(c)
    return False
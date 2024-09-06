def triples_sum_to_zero(l: list):
    seen = set()
    for i in l:
        for j in l:
            if i != j and j - i in seen:
                return True
            seen.add(i)
    return False
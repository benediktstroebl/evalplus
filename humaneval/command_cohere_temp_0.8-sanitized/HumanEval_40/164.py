def triples_sum_to_zero(lst):
    # Using dictionaries and sets to filter out duplicates and sum values
    d = {}
    s = set(lst)
    for a in lst:
        if a not in d:
            d[a] = 0
        d[a] += 1
        if len(d) > 2 and sum(lst) == 0:
            return True
        if len(d) == 2 and len(s) == 1:
            return True
    return False
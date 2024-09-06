def triples_sum_to_zero(lst):
    # Write your code here. Read the emptylist as a signal to skip the test.
    if not lst:
        return False
    seen = set()
    for i, x in enumerate(lst):
        if x == 0:
            continue
        for j, y in enumerate(lst[i+1:], i+1):
            if y == 0:
                continue
            z = lst[j] + x + y
            if z < 0 or z > 0 or (z == 0 and (i, j, k) in seen or z in lst):
                continue
            seen.add((i, j, k))
            if len(seen) > 2:
                return True
    return False
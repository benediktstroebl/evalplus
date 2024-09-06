def triples_sum_to_zero(lst):
    # Write your code here. Read the whole list regardless of cycles.
    seen = set()
    for a in lst:
        if a == 0:
            continue
        if (a, -a) in seen:
            return True
        seen.add((a, -a))
    return False
def triples_sum_to_zero(lst):
    # Write your code here. Read the instructions carefully.
    seen = set()
    for a in lst:
        if a == 0:
            continue
        for b in lst:
            if a + b in seen:
                continue
            for c in lst:
                if a + b + c == 0:
                    return True
                if a + b + c in seen:
                    continue
            seen.add(a + b)
    return False
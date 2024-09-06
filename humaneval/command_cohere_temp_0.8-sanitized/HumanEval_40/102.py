def triples_sum_to_zero(lst):
    # Write your code here. Read the markdown for more details
    seen = set()
    for a in lst:
        for b in lst:
            if a != b and sum([a, b, c]) == 0 and (a, b, c) not in seen:
                c = -a-b
                seen.add((a, b, c))
                if len(seen) == 3:
                    return True
    return False
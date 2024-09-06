def triples_sum_to_zero(lst):
    # Write your code here
    seen = set()
    for a in lst:
        for b in lst:
            if a != b and a + b in seen:
                return True
            seen.add(a)
    return False
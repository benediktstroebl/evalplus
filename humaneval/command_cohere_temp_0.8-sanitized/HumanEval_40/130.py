def triples_sum_to_zero(lst):
    # Write your code here. Read the markdown for more details
    seen = set()
    for a in lst:
        for b in lst:
            if a != b and sum(c for c in [a, b] if c in seen and c != 0) == 0:
                seen.add(a != b)
                return True
    return False
def triples_sum_to_zero(lst):
    # Write your code here. Read the problem statement again before coding.
    seen = set()
    for a in lst:
        for b in lst:
            if a != b and sum(c for c in [a, b] if c in seen and c != 0) == 0:
                return True
                seen.add(a)
                seen.add(b)
    return False
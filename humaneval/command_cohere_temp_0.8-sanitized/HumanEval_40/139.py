def triples_sum_to_zero(lst):
    # Write your code here. Read the entire file.
    seen = set()
    for a in lst:
        for b in lst:
            if a != b and sum(c for c in [a, b] if c in seen) == 0:
                seen.add(a)
                seen.add(b)
                return True
    
    return False
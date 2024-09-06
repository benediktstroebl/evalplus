def triples_sum_to_zero(lst):
    # Write your code here. Read the markdown for more info on the problem.
    seen = set()
    for a in lst:
        for b in lst:
            if a != b and sum( [a, b, c] for c in lst if c != a and c != b and not (a+b+c) in seen and not (a+b) in seen and not c in seen) == 0:
                return True
    return False
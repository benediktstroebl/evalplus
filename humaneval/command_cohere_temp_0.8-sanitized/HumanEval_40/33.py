def triples_sum_to_zero(lst):
    # Write your code here. Read the markdown code block for hints or the full solution.
    # Returned value structure:
    # True if lst has three distinct elements that sum to zero, False otherwise
    seen = set()
    for a in lst:
        if a < 0:
            continue
        for b in lst:
            if b < 0 or b == a:
                continue
            for c in lst:
                if c < 0 or c == a or c == b:
                    continue
                if a + b + c == 0 and a not in seen and b not in seen and c not in seen:
                    seen.add(a)
                    seen.add(b)
                    seen.add(c)
                    return True
    return False
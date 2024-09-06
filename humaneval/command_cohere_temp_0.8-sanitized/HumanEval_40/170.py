def triples_sum_to_zero(l: list):
    # Write your code here. Read the md block above for info on the problem.
    seen = set()
    for a in l:
        if a == 0:
            continue
        for b in l:
            if a + b in seen:
                continue
            for c in l:
                if a + b + c == 0 and a != b and a != c and b != c:
                    return True
            seen.add(a + b)
    return False
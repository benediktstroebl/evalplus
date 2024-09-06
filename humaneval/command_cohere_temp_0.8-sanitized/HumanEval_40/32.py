def triples_sum_to_zero(l: list):
    # Write your code here. Read the markdown for more details.
    seen = set()
    for a in l:
        if a != 0:
            b, c = -a, a
            if (b, c) in seen:
                return True
            seen.add((b, c))
    return False
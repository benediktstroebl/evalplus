def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0 and i not in seen and (i - 1) in seen:
            return True
        seen.add(i)
    return False
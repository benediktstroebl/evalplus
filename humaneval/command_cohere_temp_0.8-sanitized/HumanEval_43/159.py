def pairs_sum_to_zero(l):
    # Write your code here
    seen = set()
    for i in l:
        if i > 0:
            neg_i = -i
            if neg_i in seen:
                return True
            seen.add(i)
        else:
            zero_idx = l.index(i)
            if zero_idx != len(l) - 1 and l[zero_idx + 1] != 0:
                continue
            return True
    return False
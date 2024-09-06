def pairs_sum_to_zero(l):
    # Count the number of pairs
    cnt = len(l) - l.count(0) - 1
    # If there are too few, no pairs can sum to zero
    if cnt < 2:
        return False
    return any(l[i] + l[i+1] == 0 for i in range(len(l)-1))
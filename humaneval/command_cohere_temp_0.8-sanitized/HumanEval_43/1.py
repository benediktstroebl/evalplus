def pairs_sum_to_zero(l):
    # Count the number of pairs
    count = len(l) - len(set(l))
    # Count pairs that sum to zero
    zero_sum = sum([1 for i in l for j in l if i + j == 0])
    return zero_sum > 0 if count > 1 else False
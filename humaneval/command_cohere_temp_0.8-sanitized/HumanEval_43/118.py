def pairs_sum_to_zero(l):
    # Count the number of pairs
    count = len(l) - l.count(0) - 1
    # Verify if any of the pairs sum up to zero
    for i in range(len(l)-1):
        if l[i] + l[i+1] == 0:
            return True
    return bool(count)
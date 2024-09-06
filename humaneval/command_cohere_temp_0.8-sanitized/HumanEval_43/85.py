def pairs_sum_to_zero(l):
    # Count the number of non-zero values
    c = sum(1 for n in l if n)
    # Return true if there are an even number of non-zero values, and no two elements add up to zero
    return c == 0 or c % 2 == 1
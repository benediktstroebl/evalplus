def pairs_sum_to_zero(l):
    # Define the list of pairs
    pairs = list(zip(l, l[1:]))
    seen = set()
    # Check if any sum to zero
    for pair in pairs:
        if sum(pair) == 0 and pair not in seen:
            seen.add(pair)
            return True
    return False
def pairs_sum_to_zero(l):
    # Define the list of pairs to be checked
    pairs = list(zip(l, l[1:]))
    seen = set()
    for pair in pairs:
        # Check if the sum of the pair equals zero
        if sum(pair) == 0:
            # Check if the pair is unique
            if len(seen) == 0 or pair not in seen:
                return True
            seen.add(pair)
    return False
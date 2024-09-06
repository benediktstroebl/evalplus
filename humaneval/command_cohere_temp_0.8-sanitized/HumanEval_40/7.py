def triples_sum_to_zero(lst):
    # Define the variable to store whether a triplet is found
    found = False

    # Iterate over the list and check for a triplet whose sum is zero
    for a in lst:
        for b in lst:
            if a != b and sum([a, b, lst[0]]) == 0:
                found = True
                break

        # If a triplet is found, break out of the inner loop
        if found:
            break

    return found
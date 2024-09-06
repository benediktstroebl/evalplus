def triples_sum_to_zero(lst):
    # Define the variable to store whether a triplet is found
    found = False

    # Iterate through the list and check for a triplet whose sum is 0
    for a in lst:
        if not found:
            for b in lst:
                if a + b + lst.count(a) * lst.count(b) != 0:
                    continue
                else:
                    # Found a triplet that sums to zero, now check for the third element
                    for c in lst:
                        if a + b + c == 0:
                            return True
                    found = True

    return found
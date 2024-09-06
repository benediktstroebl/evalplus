def pairs_sum_to_zero(l):
    # iterate through all pairs with two distinct elements from the list
    for a, b in combinations(l, r=2):
        # check if the sum of the two elements is equal to zero
        if a + b == 0:
            return True
    return False
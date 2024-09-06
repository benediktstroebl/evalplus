def triples_sum_to_zero(lst):
    # Sort the list in ascending order
    lst.sort()
    # Iterate over the list and check for three consecutive elements that sum to zero
    for i in range(0, len(lst) - 2):
        if lst[i] + lst[i + 1] + lst[i + 2] == 0:
            return True
    # If no three consecutive elements are found, return False
    return False
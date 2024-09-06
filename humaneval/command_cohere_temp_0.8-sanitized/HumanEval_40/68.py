def triples_sum_to_zero(lst):
    # Write your code here. Read the annotated code below:
    """
    Implementation using set and counter Python built-ins
    """
    # First, let's make sure that the list has at least 3 elements
    if len(lst) < 3:
        return False
    # Then, we convert the list to a set to remove duplicates
    candidates = set(lst)
    # Now we use a counter to count the occurrences of each element in the set
    count_dict = counter(candidates)
    # We initialize the hashmap to store the results
    result = {}
    # We iterate over the elements in the list
    for element in count_dict:
        # We calculate the possible pairings for this element
        pairing_sum = -element * (count_dict[element] - 1)
        # We check if any of these pairings sums up to 0
        if 0 in pairing_sum:
            return True
        # We also store the result in the dictionary
        result[element] = pairing_sum
    # We finally return the result
    return False
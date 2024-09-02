

def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    # Your code here
    # check that list is longer than 3
    if len(l) <= 3:
        return False
    
    # find pairs which sum to zero
    # and save the pairs in a set
    pairs = set()
    for i in l:
        if -i in l:
            pairs.add(tuple(sorted([i, -i])))

    # for each pair in the set,
    # check if the set contains the
    # third number to make the sum 0
    for pair in pairs:
        # get the values out of the tuple
        a, b = pair
        # get the third value
        c = 0 - a - b
        # if the third value is in the list,
        # return True
        if c in l:
            return True

    return False



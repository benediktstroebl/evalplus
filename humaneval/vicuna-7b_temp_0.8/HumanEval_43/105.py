

def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    # base case: if the list has only one element, it cannot be pairs
    if len(l) == 1:
        return False
    
    # initialize an empty list to store the distinct elements of the list
    distinct_elements = []
    
    # iterate over the list and add each element to the list of distinct elements
    for element in l:
        distinct_elements.append(element)
    
    # check if there are two distinct elements in the list that sum to zero
    for i in range(len(distinct_elements)):
        for j in range(i + 1, len(distinct_elements)):
            if distinct_elements[i] + distinct_elements[j] == 0:
                return True
    return False

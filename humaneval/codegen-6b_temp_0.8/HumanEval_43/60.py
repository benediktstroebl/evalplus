

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
    
    # get a list of all the unique values in the list
    unique_numbers = list(set(l))
    
    # write a for loop to check if there are any duplicates in the list
    for i in unique_numbers:
        for j in unique_numbers:
            if i + j == 0 and i != j:
                return True
    return False
        

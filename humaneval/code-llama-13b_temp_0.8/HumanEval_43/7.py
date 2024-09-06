

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
    # return a boolean value
    # Hint: you may need to use the `set` data structure
    # Hint: we had a similar problem in homework 3
    # Hint: there may be a built-in function that can help you find the sum of two values

    if len(l) <= 1:
        return False
    
    sum_to_zero = False
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] + l[j] == 0:
                if i == j:
                    pass
                else:
                    sum_to_zero = True
    return sum_to_zero


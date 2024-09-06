

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
    # accumulates pairs of opposite sign and sums them
    # keeps adding the indices of the pair to a set of indices
    # does this until set has one element and the sum is 0
    # returns True if a pair of opposite sign is found and False otherwise
    
    sign_pair_sum = set()
    
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] * l[j] < 0:
                sign_pair_sum.add((i, j))
        
    return len(sign_pair_sum) == 1 and sign_pair_sum.pop() == (0, 0)
    


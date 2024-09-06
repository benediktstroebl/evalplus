

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
    # Your code here
    #create a new list to hold the result of each pair sum
    pair_sums = []
    #iterate through the list, add each element to the new list,
    # and find if the pair equals 0
    for i in l:
        if -i in l:
            pair_sums.append(-i)
    if pair_sums == []:
        return False
    else:
        return True
    



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

    if len(l) == 0 or len(l) == 1:
        return False

    #use a set to get the unique elements in the list
    #runtime complexity is O(N)
    unique_elements = set(l)

    #to check if there is a pair that sum to zero
    #we can just check if the sum of the first element in the list
    #and the last element in the list is zero.
    #runtime complexity is O(N)
    for i in range(len(l) - 1):
        if l[i] + l[-1] == 0:
            return True
    return False

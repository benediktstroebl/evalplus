

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
    # TODO: Implement triples_sum_to_zero
    # Note that this should not use a double for-loop.
    # The time complexity of your solution should be O(n)
    # Your solution should not use a single-loop solution since it will
    # give you a time complexity of O(n^2)
    # a double for loop solution will give you O(n^2)
    # but since we are only iterating over the list once, the answer
    # should be acceptable
    # Hint: You can solve this problem in a single pass through the list
    #       Keep track of two values sum_to_zero and found_one
    #       Go through the list, if you find a value that has a partner
    #       that sums to 0, then you can skip the rest of the list.
    #       If you do not find any values that sum to 0, then return
    #       False
    return False

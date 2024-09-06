

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

    # # Check if any pair of elements in the list sum to zero
    # for i in l:
    #     for j in l:
    #         if i + j == 0 and i != j:
    #             return True
    # return False

    # # Using a dictionary to keep track of previous values
    # d = {}
    # for i in l:
    #     if i in d:
    #         return True
    #     d[-i] = True
    # return False

    # Using a set to check if any two elements sum to 0
    s = set()
    for i in l:
        if 0 - i in s:
            return True
        s.add(i)
    return False



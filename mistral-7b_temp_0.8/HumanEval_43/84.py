

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

    # "I could use a dictionary to store the elements and their counts"
    dic = {}
    for num in l:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
    # "Then I'd just check if there was a -num in the dictionary, with num being the value
    # of a key in the dictionary"
    if -1 in dic:
        if dic[-1] >= 2:
            return True
    return False






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

    # time complexity: O(n^2)
    # space complexity: O(1)

    # brute force solution
    # if the list is empty
    # if len(l) == 0:
    #     return False
    # # check if there are two numbers that sum to zero
    # for i in range(0, len(l)):
    #     for j in range(i+1, len(l)):
    #         # if the sum is zero, return true
    #         if l[i] + l[j] == 0:
    #             return True
    # return False

    # time complexity: O(n)
    # space complexity: O(n)
    # hash set solution
    # use a hash set to store the elements in the list
    # the time it takes to check if an element is in the hash set is O(1)
    # O(n) to check each element, O(n) to create the set
    # O(2n) = O(n)

    # if the list is empty
    if len(l) == 0:
        return False
    # create a set
    hs = set()
    # check each element
    for x in l:
        # if the negation of the current element is in the set
        if -x in hs:
            # return True
            return True
        # otherwise add the current element to the set
        hs.add(x)
    # if we get here, there were no elements that added to zero
    return False


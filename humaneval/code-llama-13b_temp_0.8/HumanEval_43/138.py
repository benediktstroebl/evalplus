

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
    #
    # our strategy:
    #   1. use an algorithm to sort the list
    #   2. if we find two numbers that sum to zero, return True
    #   3. otherwise, return False
    #
    #   Question: can we solve this problem w/o sorting?
    #
    # you should not need to modify the test cases.
    #
    # HINT: this problem lends itself to a brute-force algorithm:
    #
    #   1. start with two nested loops
    #   2. is there a way to eliminate one of the loops?
    #
    #   QUESTION: can you see an O(n) solution?
    #
    # Note: the brute-force approach will not work if there are duplicate
    # values in the list.
    #
    # To get the runtime down to O(n), consider the following algorithm:
    #   1. make a copy of the list
    #   2. sort the copy
    #   3. consider pairs of numbers in the copy
    #
    # HINT: you may need to perform a O(n log n) sort.
    #
    # Note: do not use the sorted() function (or anything similar).
    #
    # If you complete this problem, then you should be able to pass all of
    # the other tests, as well as the bonus test.
    #
    l.sort()
    index = 0
    while index < len(l)-1:
        if l[index] + l[index+1] == 0:
            return True
        elif l[index] + l[index+1] > 0:
            return False
        index += 1
    return False


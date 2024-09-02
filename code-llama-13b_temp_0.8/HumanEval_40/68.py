

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
    # Hint: keep a running list of the seen items in the list
    # and check to see if there are 3 items that sum to zero
    # after each iteration through the list.
    # You may find it useful to initialize seen to be a dict
    # mapping integers to booleans.

    # time complexity O(n^2)
    # space complexity O(n)

    # seen = dict()
    # for num1 in l:
    #     for num2 in l:
    #         if (num1 + num2) in seen:
    #             return True
    #         seen[num1 + num2] = True
    # return False

    # time complexity O(n^2)
    # space complexity O(1)
    seen = set()
    for num1 in l:
        for num2 in l:
            if (num1 + num2) in seen:
                return True
            seen.add(num1 + num2)
    return False


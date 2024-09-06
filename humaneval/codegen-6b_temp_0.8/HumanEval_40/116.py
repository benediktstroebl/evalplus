

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
    positive_nums = set()
    negative_nums = set()
    zero_nums = set()

    for num in l:
        if num > 0:
            positive_nums.add(num)
        elif num < 0:
            negative_nums.add(num)
        else:
            zero_nums.add(num)

    for elem in positive_nums:
        if (-elem) in negative_nums:
            return True

    return False

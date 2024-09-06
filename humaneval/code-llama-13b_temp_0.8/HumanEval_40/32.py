

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
    # store each number as a dictionary key
    # value is number of occurences of the key
    dictionary = {}
    for number in l:
        if number in dictionary:
            dictionary[number] += 1
        else:
            dictionary[number] = 1

    # return True if there are three distinct numbers that sum to zero.
    for num in dictionary:
        # If there is another num such that
        # num + num + (-2 * num) = 0
        # which is true if and only if
        # 2 * num = num + num + (-num) = 0
        if 2 * num in dictionary:
            return True

    return False

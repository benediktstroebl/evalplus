

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
    positive_numbers = []
    negative_numbers = []

    for number in l:
        if number > 0:
            positive_numbers.append(number)
        elif number < 0:
            negative_numbers.append(number)

    for n1 in positive_numbers:
        for n2 in negative_numbers:
            if n1 + n2 == 0:
                return True

    return False


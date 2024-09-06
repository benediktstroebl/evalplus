

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
    negative_index = 0
    positive_index = 0
    negative_sum = 0
    positive_sum = 0
    #iterate the list from both ends
    while negative_index < len(l):
        negative_sum += l[negative_index]
        positive_sum += l[positive_index]
        if negative_sum == positive_sum:
            return True
        elif negative_sum > positive_sum:
            negative_index += 1
        else:
            positive_index += 1
    return False

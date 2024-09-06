

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
    # 1. split the list into two lists
    nums_and_neg = list(l)
    positive_nums = [x for x in nums_and_neg if x >= 0]
    negatives = [x for x in nums_and_neg if x < 0]
    # 2. check if there are any negative numbers
    if negatives:
        return False
    # 3. check if there are two distinct positive numbers
    if len(positive_nums) != 2:
        return False
    # 4. check if the two positive numbers add up to zero
    if sum(positive_nums) != 0:
        return False
    # 5. check if there are any remaining positive numbers
    if len(positive_nums) > 0:
        return True
    return False
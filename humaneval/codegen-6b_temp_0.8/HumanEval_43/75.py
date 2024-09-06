

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
    # Create a dictionary of the numbers in the list and
    # values that are how many times they appear in the list
    nums = {}
    for num in l:
        if num in nums:
            nums[num] += 1
        else:
            nums[num] = 1
    # Iterate through the dictionary comparing each value
    # to the next item in the dictionary
    for i in range(len(l)):
        if -l[i] in nums:
            if nums[-l[i]] > 1:
                return True
    return False
    
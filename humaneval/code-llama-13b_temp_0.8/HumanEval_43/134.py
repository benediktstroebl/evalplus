

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
    n = len(l)
    # Steps:
    # 1. initialize a set to store the numbers that sum to 0
    # 2. iterate through the list
    # 3. If the number is zero, return True
    # 4. if the number's negation is in the set, return True
    # 5. else, add the number to the set
    # 6. return False

    # 1. initialize a set to store the numbers that sum to 0
    s = set()
    # 2. iterate through the list
    for i in range(n):
        # 3. If the number is zero, return True
        if l[i] == 0:
            return True
        # 4. if the number's negation is in the set, return True
        if l[i] in s:
            return True
        # 5. else, add the number to the set
        s.add(l[i])
    # 6. return False
    return False

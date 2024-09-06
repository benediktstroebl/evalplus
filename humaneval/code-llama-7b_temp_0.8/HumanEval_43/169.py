

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

    # your code here
    # pass

    # time O(n) because we are traversing all elements
    # space O(n) because we are storing all elements in a dictionary
    if l == []:
        return False
    if len(l) == 1:
        return False
    # dict_nums = {}
    # for num in l:
    #     if num in dict_nums:
    #         return True
    #     else:
    #         dict_nums[num] = 1
    # return False

    # time O(nlogn) because we are using sorting
    # space O(1) because we are not using extra space
    # l = sorted(l)
    # i = 0
    # j = len(l) - 1
    # while i < j:
    #     if l[i] + l[j] == 0:
    #         return True
    #     if l[i] + l[j] > 0:
    #         j -= 1
    #     if l[i] + l[j] < 0:
    #         i += 1
    # return False

    # time O(n^2) because we are using nested loop
    # space O(1) because we are not using extra space
    # for i in range(len(l)):
    #     for j in range(i + 1, len(l)):
    #         if l[i] + l[j] == 0:
    #             return True
    # return False

    # time O(n) because we are traversing all elements
    # space O(1) because we are not using extra space
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == 0:
                return True
    return False


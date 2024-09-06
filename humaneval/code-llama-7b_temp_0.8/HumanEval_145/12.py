
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    # for every element of the list
    # iterate over the elements and
    # sum the digits
    # sum all the sums
    # make a dictionary and
    # set the sum to be the key and the value to be the list item
    # sort the dictionary by key
    # reverse the dictionary
    # make a list out of the dictionary
    # return the list
    dict1 = {}
    dict2 = {}
    i = 0
    for item in nums:
        sum1 = 0
        while item > 0:
            sum1 += item % 10
            item = item // 10
        if sum1 not in dict1:
            dict1[sum1] = [nums[i]]
        else:
            dict1[sum1].append(nums[i])
        i += 1
    list1 = list(dict1.keys())
    list1.sort()
    list2 = list1[::-1]
    i = 0
    for item in list2:
        for num in dict1[item]:
            dict2[num] = item
        i += 1
    return dict2


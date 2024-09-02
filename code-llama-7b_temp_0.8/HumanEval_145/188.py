
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

    # create a dictionary, with sum of digits as key and number as value
    d = {}
    for i in nums:
        sum_of_digits = 0
        for j in str(i):
            sum_of_digits += int(j)
        d[sum_of_digits] = i

    # iterate through the dictionary values
    # and add to final list
    # based on the index
    lst = []
    for k in sorted(d):
        lst.append(d[k])

    return lst


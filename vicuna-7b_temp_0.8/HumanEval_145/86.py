
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
    # sort the list
    nums = sorted(nums)

    # initialize the result list
    result = []

    # iterate over the sorted list
    for num in nums:
        # find the index of the first non-zero digit
        i = 0
        while num[i] == '0':
            i += 1

        # add the number and the digit and subtract the digit
        result.append(num[i:])
        result.append(num[i])

        # remove the digit and the number
        num.pop(i)

    return result
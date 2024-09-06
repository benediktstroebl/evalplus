
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
    # sort the list first
    nums.sort()

    # initialize the result list
    result = []

    # while the list is not empty
    while nums:
        # find the first non-negative number
        while True:
            num = nums.pop(0)
            if num >= 0:
                break

        # add the number to the result list
        result.append(num)

        # find the next number with the same sum of digits
        num = nums.pop(0)
        while True:
            if num >= 0:
                break
            remainder = num % 10
            num = num // 10
            if remainder != remainder // 10:
                break

        # add the next number to the result list
        result.append(num)

    return result
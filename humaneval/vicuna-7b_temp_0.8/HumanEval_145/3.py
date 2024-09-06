
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
    # This is a new list to store the sorted list
    result = []

    # Loop through the input list
    for num in nums:
        # If the num is negative, adjust the index by 1
        if num < 0:
            num = num + 1

        # If the num is the first one, adjust the index by 2
        if num == 0:
            num = num + 2

        # If the sum of the digits is 0, adjust the index by 3
        if sum(map(int, str(num))) == 0:
            num = num + 3

        # Add the num to the result list
        result.append(num)

    return result

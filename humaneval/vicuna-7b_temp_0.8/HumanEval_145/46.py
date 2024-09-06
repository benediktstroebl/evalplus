
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
    # ensure the list of integers is not empty
    if not nums:
        return []

    # initialize result list
    result = []

    # sort the list based on the sum of digits
    for num in nums:
        index = num // 10
        digit = num % 10
        result.append((index, digit))
        result.append(num)

    # sort the result list based on the sum of digits
    result.sort(key=lambda x: x[1] + x[0])

    return [num for _, num in result]

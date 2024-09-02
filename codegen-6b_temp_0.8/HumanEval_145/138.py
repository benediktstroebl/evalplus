
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
    result = []

    for num in nums:
        number_sum = 0
        for digit in str(num):
            number_sum += int(digit)

        result.append((number_sum, num))

    result.sort()
    sorted_nums = [elem[1] for elem in result]

    return sorted_nums


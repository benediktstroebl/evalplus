
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
    new_nums = []
    for num in nums:
        sum_digits = 0
        while num > 0:
            sum_digits += num % 10
            num //= 10
        new_nums.append((sum_digits, num))
    new_nums.sort(key=lambda tup: tup[0])
    new_nums.sort(key=lambda tup: tup[1])
    return [num for num, digits in new_nums]



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
    # Calculate the sum of digits of each number in the list
    sum_of_digits = [sum(int(digit) for digit in str(num)) for num in nums]

    # Sort the list of numbers based on the sum of their digits
    sorted_nums = sorted(nums, key=lambda num: sum_of_digits[nums.index(num)])

    return sorted_nums



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
    # two-pass algorithm:
    # 1. convert input list to a list of tuples where each tuple contains a digit and an index
    digits_and_indices = [(sum(int(digit) for digit in str(num)), i) for i, num in enumerate(nums)]
    # 2. sort the list of tuples based on the sum of digits
    digits_and_indices.sort(key=lambda x: x[1], reverse=True)
    # 3. reverse the order of the tuples so that the original numbers are restored
    return [nums[i] for i, num in enumerate(digits_and_indices[::-1])]

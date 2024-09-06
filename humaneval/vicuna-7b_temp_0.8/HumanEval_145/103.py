
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
    # Check if the list is empty
    if not nums:
        return []

    # Create a dictionary that maps each digit (0-9) to its position
    # in the original list
    digits = {digit: i for i, digit in enumerate(nums)}

    # Find the maximum sum of digits in the list
    max_sum = max(sum(map(lambda x: sum(map(lambda y: ord(y) - ord('0'), x)), digits)) for _, x in enumerate(nums))

    # Sort the list according to the sum of its digits
    return sorted(nums, key=lambda x: sum(map(lambda y: ord(y) - ord('0'), x)))

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
    # Convert input list to a list of integers using Python's built-in function list(nums)
    nums_int = list(nums)

    # Sort the list
    nums_int.sort(key=lambda x: sum(int(i) for i in str(x)))

    # Convert the sorted list back to a list of numbers
    return [int(i) for i in str(nums_int[0])]

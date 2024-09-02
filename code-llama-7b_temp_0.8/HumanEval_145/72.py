
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
    # calculate sum of digits in each number
    # sort by sum of digits in descending order
    # if two numbers have same sum, order them by index

    # sort by sum
    nums.sort(key=lambda x: sum(int(i) for i in str(x)))

    # sort by index
    nums.sort(key=lambda x: x)

    return nums


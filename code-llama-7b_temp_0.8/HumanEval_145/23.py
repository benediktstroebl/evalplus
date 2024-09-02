
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

    if not nums:
        return []

    sum_dict = {}

    # Get the sum of all numbers
    for i in nums:
        sum_dict[i] = sum([int(i) for i in str(i)])

    # Order by sum of the number
    ordered_nums = sorted(sum_dict.items(), key=lambda x: x[1])

    # Sort the original list based on the new ordered list
    ordered_nums_list = [i[0] for i in ordered_nums]

    return ordered_nums_list


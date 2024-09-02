
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
    nums_dict = {}
    for num in nums:
        if sum(int(i) for i in str(num)) not in nums_dict:
            nums_dict[sum(int(i) for i in str(num))] = []
        nums_dict[sum(int(i) for i in str(num))].append(num)
    result = []
    for key in sorted(nums_dict.keys()):
        for num in nums_dict[key]:
            result.append(num)
    return result


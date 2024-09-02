
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
    n = len(nums)
    if n == 0:
        return []
    sum_list = [sum(int(d) for d in str(num)) for num in nums]
    sum_dict = {num: sum(int(d) for d in str(num)) for num in nums}
    result = sorted(sum_list, key=sum_dict.get, reverse=True)
    result = sorted([num for num, _ in result], key=lambda x: x if x is not None else -1)
    return [num for num, _ in result]

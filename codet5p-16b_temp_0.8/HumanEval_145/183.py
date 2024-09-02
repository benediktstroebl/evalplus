
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

    sorted_list = []
    new_list = []
    for i in nums:
        new_list.append(sum(list(map(int, str(i)))))
    sorted_list = sorted(new_list)
    for i in sorted_list:
        for j in nums:
            if i == sum(list(map(int, str(j)))):
                sorted_list.append(j)
    return sorted_list


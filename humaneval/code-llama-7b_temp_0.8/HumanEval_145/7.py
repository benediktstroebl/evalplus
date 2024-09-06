
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
    # nums_list = list(nums)
    nums_list = nums
    new_nums = []

    if not nums_list:
        return []

    for i in nums:
        # new_nums = []
        digits = []
        for d in str(i):
            digits.append(d)
        digits = int(''.join(digits))
        new_nums.append((digits, i))
        # new_nums.sort()

    new_nums.sort(key=lambda x: x[0])
    for i in new_nums:
        i = i[1]
        nums_list.remove(i)
        nums_list.append(i)

    return nums_list
















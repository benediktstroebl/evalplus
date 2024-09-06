
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

    if len(nums) == 1:
        return nums

    def _order_by_points(nums):
        d_nums = {}
        for num in nums:
            s = sum(int(str(num)[i]) for i in range(len(str(num))))
            d_nums.setdefault(s, [])
            d_nums[s].append(num)

        return [item[0] for item in sorted(d_nums.items(), key=lambda x: x[0])]

    return _order_by_points(nums)


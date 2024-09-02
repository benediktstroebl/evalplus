
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
    # nums = list(nums)
    # index_dict = {}
    # for i in range(len(nums)):
    #     index_dict[i] = sum(list(map(int, str(nums[i]))))
    #
    # return [nums[i] for i in sorted(index_dict, key=index_dict.get, reverse=False)]
    return sorted(nums, key=lambda x: (sum(map(int, str(x))), x))

    # sort_nums = []
    # for n in nums:
    #     sort_nums.append((sum(list(map(int, str(n)))), n))
    # sort_nums.sort(key=lambda x: x[0])
    # return [n[1] for n in sort_nums]

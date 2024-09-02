
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
    # for n in nums:
    #     print(sum(map(int, str(n))))
    # return nums

    # for idx, item in enumerate(nums):
    #     new_sum = sum(map(int, str(item)))
    #     new_item = (new_sum, idx, item)
    #     print(new_item)
    #
    #     nums.insert(idx, new_item)
    #
    # return [item for _, _, item in sorted(nums)]


    # nums = [sum(map(int, str(x))) for x in nums]
    # return [x for _, x in sorted(zip(nums, nums))]

    # return sorted(nums, key=lambda x: sum(int(i) for i in str(x)))

    # return sorted(nums, key=lambda x: (sum(int(i) for i in str(x)), x))
    # return [x for _, x in sorted(zip(map(sum, map(int, str)), nums))]





    # for idx, item in enumerate(nums):
    #     new_sum = sum(map(int, str(item)))
    #     new_item = (new_sum, idx, item)
    #     print(new_item)
    #
    #     nums.insert(idx, new_item)
    #
    # return [item for _, _, item in sorted(nums)]



    # return [item for _, _, item in sorted(zip(map(sum, map(int, str)), enumerate(nums)))]



    # return [x for _, x in sorted(zip(map(sum, map(int, str)), nums))]





    # return [x for _, x in sorted(zip(map(sum, map(int, str)), nums))]

    # for idx, item in enumerate(nums):
    #     new_sum = sum(map(int, str(item)))
    #     new_item = (new_sum, idx, item)
    #     print(new_item)

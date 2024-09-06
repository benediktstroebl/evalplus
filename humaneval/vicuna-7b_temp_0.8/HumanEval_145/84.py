
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
    # sort the list
    nums.sort()

    # build a map of numbers to their index
    index_map = {num: i for i, num in enumerate(nums)}

    # sum of digits of each number is same as its index
    for i in range(len(nums)):
        digits = sum(str(num) for num in nums[:i+1])
        digits = [d if d > 9 else d - 2 if d >= 0 else 2*d - 1 for d in digits]
        for j in range(i + 1, len(nums)):
            num_index = index_map[nums[j]]
            if digits[num_index] > digits[nums[i]]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums
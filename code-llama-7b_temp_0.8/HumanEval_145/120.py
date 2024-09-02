
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
    print(nums)
    if len(nums) == 0:
        return []
    index = 0
    while index < len(nums):
        j = 0
        while j < len(nums):
            if sum(int(i) for i in str(nums[index])) > sum(int(i) for i in str(nums[j])):
                nums[j], nums[index] = nums[index], nums[j]
            if sum(int(i) for i in str(nums[index])) == sum(int(i) for i in str(nums[j])):
                if nums[j] < nums[index]:
                    nums[j], nums[index] = nums[index], nums[j]
            j += 1
        index += 1
    return nums

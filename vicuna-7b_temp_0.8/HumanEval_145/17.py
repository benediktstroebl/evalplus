
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
    # use a list to store the numbers with same sum of digits
    digits = []
    for num in nums:
        digits.append(str(num))
        while str(num) in digits:
            num = num / 10
            digits.append(str(num))
    sorted_nums = sorted(digits, key=lambda x: x.isdigit() and int(x) + int(str(nums.index(nums.remove(nums[0])))))
    return nums[nums.index(nums[0]):nums.index(nums[-1])+1] + sorted_nums

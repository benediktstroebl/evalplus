
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
    # print(nums)
    new_nums = []
    for num in nums:
        if num < 0:
            sum_num = sum(int(digit) for digit in str(num)[1:])
            new_nums.append(-num * sum_num)
        else:
            sum_num = sum(int(digit) for digit in str(num))
            new_nums.append(num * sum_num)
    
    # print(new_nums)
    return sorted(new_nums, key=lambda x: (x % abs(x), abs(x)))

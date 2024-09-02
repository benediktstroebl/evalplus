
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
    result = []
    for num in nums:
        if num == 0:
            result.append(num)
            continue

        sum_num = 0
        negative = num < 0
        num = abs(num)
        while num:
            sum_num += num % 10
            num //= 10
        result.append(negative * -sum_num)

    return [nums[i] for _, i in sorted(zip(result, range(len(nums))))]

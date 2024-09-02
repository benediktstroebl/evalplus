
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
        while True:
            digit = sum(int(digit) for digit in str(num))
            if digit == 0:
                break
            if num - int(str(num)[-1]) * 100 + int(str(num)[-2]) * 10 + int(str(num)[-3]) * 1 + 1 > 0:
                break
            result.append(num)
            num = str(num)
    return result
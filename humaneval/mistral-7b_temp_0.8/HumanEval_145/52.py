
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
    digits = []
    for number in nums:
        digits.append(number)
        num_string = str(number)
        sum_of_digits = 0
        for i in num_string:
            sum_of_digits += int(i)
        digits.append(sum_of_digits)
    digits.sort()
    return [i for i in digits[0::2]]

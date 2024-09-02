
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
    # convert input list to list of digits
    digits = [int(n) for n in nums]
    # sort digits
    digits.sort()
    # convert digits to list of integers
    nums = [digits.pop(0)]
    while digits:
        # find two digits with the most digits
        digit1 = digits.pop(0)
        digit2 = digits.pop(0)
        # add digit1 and digit2 and subtract from the next digit
        nums.append(digit1 + digit2)
        nums.append(nums[-1] - digit1 - digit2)
        # remove digit1, digit2
        digits = [d - (digit1 + digit2) for d in digits]
    return nums

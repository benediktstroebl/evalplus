
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
    # create a new list to store results
    nums_new = []
    # loop through the given list
    for num in nums:
        # calculate the sum of the digits of the number
        sum_digits = sum([int(digit) for digit in str(num)])
        # append the number to the new list, sorted by the sum of its digits
        nums_new.append((num, sum_digits))
    # sort the new list by the second element (the sum of the digits)
    nums_new.sort(key=lambda x: x[1])
    # loop through the new list
    for num, sum_digits in nums_new:
        # append the number to the original list, sorted by the sum of its digits
        nums.append(num)
    return nums

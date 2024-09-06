
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
    sorted_nums = sorted(nums)

    # for each number, keep only the digits and sum them
    digits = [digit for num in sorted_nums for digit in str(num)]
    digit_sums = [sum(map(int, digit_str)) for digit_str in digits]

    # initialize variables to keep track of the number and sum of digits
    # for each number in the list
    nums_index = [0] * len(digits)
    digit_sums_index = [0] * len(digit_sums)

    # update the values of nums_index and digit_sums_index
    for i, num in enumerate(sorted_nums):
        for j, digit in enumerate(str(num)):
            nums_index[j] += int(digit)
            digit_sums_index[j] += digit_sums[i]

    # return the sorted list
    return [nums_index[i] for i in range(len(nums_index))]
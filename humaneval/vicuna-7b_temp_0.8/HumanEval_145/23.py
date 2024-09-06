
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
    # This function uses a dictionary to count the sum of digits for each number
    # in the list. It then sorts the list by the values in the dictionary.

    # Keep track of the sum of the digits for each number in the list
    sums = {}
    for num in nums:
        digit_sum = sum(int(num) for num in str(num))
        if num in sums:
            sums[num] += digit_sum
        else:
            sums[num] = digit_sum

    # Sort the list by the values in the dictionary
    result = sorted(sums.items(), key=lambda x: x[1], reverse=True)

    return [x[0] for x in result]

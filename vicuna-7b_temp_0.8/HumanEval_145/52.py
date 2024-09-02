
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
    # This is not efficient.
    # It uses two loops to iterate through the input list twice.
    # It would be faster to use a single loop and a dictionary to keep track of the sums.

    # Initialize the dictionary to store the sums and their indices
    sums_and_indices = {}

    # Iterate through the input list and compute the sum of digits
    # for each item in the list
    for num in nums:
        digit_sum = 0
        for digit in str(num):
            digit_sum += digit - '0'
        digit_sum = digit_sum // 10
        index = num - digit_sum * 10
        sums_and_indices[index] = num

    # Sort the input list by computing the index of each item
    # and then sorting the list according to the values of the index
    sorted_nums = sorted(sums_and_indices.items(), key=lambda x: x[1])

    return [nums[i] for i in sorted_nums]

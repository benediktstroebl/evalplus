
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
    # Use a dictionary to store the sum of digits of each number
    # and its index in the original list
    sums_and_indices = {}

    for number in nums:
        digit_sum = sum(digit * (i + 1) for i, digit in enumerate(str(number)))
        if digit_sum in sums_and_indices:
            # If the sum has already been processed,
            # use its index in the original list
            return [nums[index] for index in sums_and_indices[digit_sum]]

        # If the sum has not been processed,
        # store it in the dictionary
        sums_and_indices[digit_sum] = len(nums)

        # Update the sum of digits for this number
        digit_sum = sum(digit * (i + 1) for i, digit in enumerate(str(number)))
        sums_and_indices[digit_sum] = len(nums)

        # Sort the number based on the sum of its digits
        # and then its index in the original list
        return [nums[index] for index in sorted(sums_and_indices[digit_sum])]

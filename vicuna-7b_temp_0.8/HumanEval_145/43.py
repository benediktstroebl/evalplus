
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
    # Use a variable to store the running sum
    # and a variable to store the current index
    current_sum = 0
    current_index = 0

    # Iterate over the list of integers
    for num in nums:
        # Add the digits of the number and
        # update the sum and index
        current_sum += num
        current_index += 1

        # If the sum is greater than 9,
        # subtract 1 from the sum
        if current_sum >= 10:
            current_sum -= 10
        else:
            # Store the number in a variable
            # and update the current sum and index
            nums[current_index - 1] = current_sum
            current_sum = num

    return nums
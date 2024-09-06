
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
    # Check if the input list is empty or not
    if not nums:
        return []

    # Create a dictionary to store the sum of digits for each number
    num_dict = {}
    for num in nums:
        digit_sum = sum(int(digit) for digit in str(num))
        num_dict[num] = digit_sum

    # Sort the list of numbers based on their sum of digits
    sorted_list = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)

    # Convert the list of tuples to a list
    return [nums[i] for i in sorted_list]

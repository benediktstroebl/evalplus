def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers based on their index in the original list.

    Args:
        nums (list): List of integers

    Returns:
        list:Sorted list based on criteria above
    """
    if not nums:
        return []

    def sum_digits(num):
        total = 0
        for digit in str(num):
            total += int(digit)
        return total

    sorted_nums = sorted(nums, key=lambda x: (sum_digits(x), x))
    return sorted_nums
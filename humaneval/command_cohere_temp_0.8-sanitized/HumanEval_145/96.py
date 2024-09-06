def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers based on their index in the original list.

    Args:
        nums (list): List of integers

    Returns:
        list: Ordered list based on the criteria specified.
    """
    if len(nums) <= 1:
        return nums
    digit_sums = [sum(map(int, str(num))) for num in nums]
    sorted_digits = sorted(zip(digit_sums, nums), key=lambda x: (x[0], x[1][0]))
    return [i[1] for i in sorted_digits]
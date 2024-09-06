def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Args:
        nums (list): List of integers

    Returns:
        list: Ordered list based on criteria above
    """
    if not nums:
        return []

    # Calculate the digit-sum-sorted order without tiebreakers, using the default sorting
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]
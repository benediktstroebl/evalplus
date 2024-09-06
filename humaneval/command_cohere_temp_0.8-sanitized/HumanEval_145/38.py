def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list:Sorted list based on the criteria.
    """
    if len(nums) == 0:
        return []

    # Compute the digit-based score for each number
    def digit_score(num):
        score = 0
        for digit in str(num):
            score += int(digit)
        return score

    # Sort based on digit score and original index
    sorted_nums = sorted(nums, key=lambda x:[digit_score(x), x])
    return sorted_nums
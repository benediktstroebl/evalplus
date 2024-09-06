import unittest
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.
    """
    if not nums:
        return []

    # Calculate the total digit sum for each number and sort them accordingly.
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]
    sorted_idx = sorted(range(len(nums)), key=lambda i: digit_sums[i])

    # Reconstruct the sorted list using the original numbers and their sorted indices.
    sorted_nums = [nums[i] for i in sorted_idx]
    return sorted_nums
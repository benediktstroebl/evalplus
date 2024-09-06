def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tie breaks determined by the index of the integer in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Sortedd list based on criteria.
    """
    if not nums:
        return []

    summed_digits = []
    original_indices = [i for i, n in enumerate(nums)]

    for n in nums:
        sum_digits = sum(int(d) for d in str(n))
        summed_digits.append((sum_digits, i))

    # Sort based on sum of digits with tie breaks based on original index
    sorted_nums = sorted(nums, key=lambda n: summed_digits.index(
        (summed_digits.count(n[0]), n[1])))

    return sorted_nums
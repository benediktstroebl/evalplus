def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # Calculate the digit-based score of each number
    scores = [sum(int(d) for d in str(n)) for n in nums]

    # Apply tiebreaks by sorting by original index
    sorted_nums = sorted(zip(nums, scores), key=lambda x: (x[1], x[0]))

    # Extract the sorted numbers and return
    return [n for n, _ in sorted_nums]
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list based on the criteria.
    """
    if not nums:
        return []

    # Helper function to compare two numbers with sum-of-digits tiebreaker.
    def compare(a, b):
        if sum_digits(a) != sum_digits(b):
            return sum_digits(a) - sum_digits(b)
        return idx(a) - idx(b)

    # Sort the list based on the sum-of-digits criteria.
    nums.sort(key=lambda x: (sum_digits(x), idx(x)))

    return nums
def sum_digits(n):
    return sum(int(d) for d in str(n))
def idx(n):
    return nums.index(n) if n in nums else len(nums)
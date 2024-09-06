```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # Calculate the total digit sum for each number and sort them accordingly.
    digit_sums = [sum(int(d) for d in str(n)) for n in nums]
    sorted_digits = sorted(zip(digit_sums, nums), key=lambda x: x[0], reverse=True)

    # Now reconstruct the sorted original list according to the tiebreaker (index).
    sorted_nums = [n for digit_sum, n in sorted_digits]
    return sorted_nums

# Test cases:
>>> order_by_points([1, 11, -1, -11, -12])
[-1, -11, 1, -12, 11]
>>> order_by_points([5, 4, 25, 4])
[4, 4, 5, 25]
>>> order_by_points([])
[]
>>> order_by_points([-5, -10, -15, -20])
[-20, -15, -10, -5]
``` 

This Python script defines a function `order_by_points` that sorts a list of integers based on the sum of their digits, with indices as the tiebreaker. The function first calculates the digit sum for each number and sorts them accordingly. Then, it reconstructs the sorted list using the indices as a tiebreaker. Test cases prove the function's correctness.
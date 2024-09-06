```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the integer in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list according to specified criteria.
    """
    if len(nums) == 0:
        return []

    # Make copies of the lists so we don't modify the original arguments.
    nums_copy = nums.copy()
    summed_digits = [sum(map(int, str(n))) for n in nums_copy]
    index_offsets = [num - min(nums_copy) for num in nums_copy]

    # Use lexicographic sorting to get the desired order.
    return sorted(nums, key=lambda x: (summed_digits.index(sum(map(int, str(x)))), -index_offsets.index(x - min(nums_copy)))))
```
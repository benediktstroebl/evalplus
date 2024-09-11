```python
def pairs_sum_to_zero(nums):
    """
    Returns True if there are two distinct elements in the list that sum to zero, and False otherwise.

    Args:
    nums (list): A list of integers.

    Returns:
    bool: Whether a pair of distinct elements sums to zero.
    """
    seen = set()
    for num in nums:
        if -num in seen:
            return True
        seen.add(num)
    return False

# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script defines a function `pairs_sum_to_zero` that checks whether two distinct elements in the input list sum to zero. It does this by maintaining a set `seen` of the elements it has encountered so far. If it encounters an element that is the negation of an element it has already seen, it immediately returns `True`. If it has checked all the elements and not found a pair that sums to zero, it returns `False`.
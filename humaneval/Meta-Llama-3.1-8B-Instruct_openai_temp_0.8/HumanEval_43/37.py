### pairs_sum_to_zero Function
```python
def pairs_sum_to_zero(nums):
    """
    Returns True if there are two distinct elements in the list that sum to zero, and False otherwise.

    Args:
        nums (list): A list of integers.

    Returns:
        bool: Whether two distinct elements sum to zero.
    """
    seen = set()
    for num in nums:
        complement = -num
        if complement in seen:
            return True
        seen.add(num)
    return False

# Example usage:
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))   # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))          # False
```

This function iterates over the input list `nums`. For each number, it checks if its complement (`-num`) is already present in the `seen` set. If it is, the function immediately returns `True` because it has found two distinct elements that sum to zero. If it hasn't found such a pair after checking all numbers, it returns `False`. The `seen` set keeps track of the numbers that have been seen so far, ensuring that each number is only checked once.
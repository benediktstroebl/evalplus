```python
def pairs_sum_to_zero(nums):
    """
    Checks if there are two distinct elements in the list that sum up to zero.

    Args:
        nums (list): A list of integers.

    Returns:
        bool: True if such pair exists, False otherwise.
    """
    seen = set()
    for num in nums:
        if -num in seen:
            return True
        seen.add(num)
    return False
```
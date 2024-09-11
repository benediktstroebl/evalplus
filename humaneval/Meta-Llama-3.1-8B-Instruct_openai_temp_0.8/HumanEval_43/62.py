```python
def pairs_sum_to_zero(nums):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.

    Args:
        nums (list): A list of integers.

    Returns:
        bool: True if there are two distinct elements that sum to zero, False otherwise.
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

This script uses a set to keep track of the numbers it has seen so far. If it encounters a number that is the negative of a number it has seen before, it returns True, indicating that there are two numbers that sum to zero. If it iterates over all numbers in the list without finding a pair that sums to zero, it returns False.
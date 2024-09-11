```python
def monotonic(nums: list):
    """
    Check if a list of numbers is monotonically increasing or decreasing.

    Args:
        nums (list): A list of numbers.

    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    is_increasing = all(nums[i] <= nums[i+1] for i in range(len(nums)-1))
    is_decreasing = all(nums[i] >= nums[i+1] for i in range(len(nums)-1))
    
    return is_increasing or is_decreasing

# Test the function
print(monotonic([1, 2, 4, 20]))  # Expected: True
print(monotonic([1, 20, 4, 10]))  # Expected: False
print(monotonic([4, 1, 0, -10]))  # Expected: True
```

In this script, the `monotonic` function uses list comprehension and the `all` function to check whether the list is monotonically increasing (`is_increasing`) or decreasing (`is_decreasing`). The function then returns `True` if either condition is met, and `False` otherwise. The test cases demonstrate the function's usage.
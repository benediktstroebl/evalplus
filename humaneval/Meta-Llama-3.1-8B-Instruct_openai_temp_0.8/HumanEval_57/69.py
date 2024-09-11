```markdown
### Monotonic List Checker

This script checks if a given list of numbers is monotonically increasing or decreasing.

#### Code
```python
def monotonic(nums: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        nums (list): A list of numbers.

    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.

    Examples:
        >>> monotonic([1, 2, 4, 20])
        True
        >>> monotonic([1, 20, 4, 10])
        False
        >>> monotonic([4, 1, 0, -10])
        True
    """
    return len(set(nums)) == 1 or (all(nums[i] <= nums[i+1] for i in range(len(nums)-1)) or all(nums[i] >= nums[i+1] for i in range(len(nums)-1)))

# Test the function
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([1, 1, 1, 1]))  # True
print(monotonic([1, 2, 3, 4, 5]))  # True
print(monotonic([5, 4, 3, 2, 1]))  # True
print(monotonic([2, 2, 2, 2]))  # True
```

#### Explanation

The function `monotonic` takes a list of numbers as input and returns `True` if the list is monotonically increasing or decreasing, and `False` otherwise. It uses the `all` function to check if all pairs of adjacent elements in the list are either in increasing or decreasing order.

If the list contains all the same numbers, it returns `True` because an increasing/decreasing list can also be considered a special case of monotonic where each number is equal to the next one (of course we can only do this if they are all the same).
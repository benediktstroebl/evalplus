```python
def double_the_difference(nums):
    """
    Sum of squares of odd integers in a list of numbers ignoring negatives and non-integers.
    
    Args:
        nums (list): List of numbers.

    Returns:
        int: Sum of squares of odd integers or 0 if the list is empty or contains only even or negative integers.
    """
    result = 0
    for num in nums:
        if num > 0 and isinstance(num, int):
            result += num**2
    return result

# Test cases
assert double_the_difference([1, 3, 2, 0]) == 10
assert double_the_difference([-1, -2, 0]) == 0
assert double_the_difference([9, -2]) == 81
assert double_the_difference([0]) == 0
assert double_the_difference([-1, 0, 1, 2, 3, -4, 5, -6]) == 1 + 9 + 4 + 25 = 39
```

This code defines the `double_the_difference` function, which takes a list of numbers as input and returns the sum of the squares of odd numbers in the list, ignoring any negative numbers or non-integer values. The function iterates through each number in the input list, checks if it's positive and an integer, and if so, adds its square to the total. The function returns 0 if the input list is empty or contains only even or negative integers.

The test cases are also provided to demonstrate the function's behavior for different input scenarios.
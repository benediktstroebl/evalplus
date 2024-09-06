Here's a Python function that solves the given problem and includes informative commentary to explain its logic:
```python
def double_the_difference(lst):
    """
    Sum of squares of odd numbers in a list, while ignoring negative or non-integer numbers.

    Args:
        lst (list): List of numbers.

    Returns:
        int: Sum of squares of odd numbers, or 0 if the list is empty or contains only even or negative numbers.
    """
    result = 0
    # Initialize a flag to track if any valid odd number is found.
    found_valid_odd = False
    
    # Iterate through the list and check for valid odd numbers.
    for num in lst:
        if isinstance(num, int) and num > 0 and (num % 2) != 0:
            found_valid_odd = True
            # Square the number and add it to the result.
            result += num ** 2
    
    # If no valid odd numbers are found, return 0.
    if not found_valid_odd:
        return 0
    
    return result

# Test cases
assert double_the_difference([1, 3, 2, 0]) == 10
assert double_the_difference([-1, -2, 0]) == 0
assert double_the_difference([9, -2]) == 81
assert double_the_difference([0]) == 0  # Edge case: Empty list
```

This function incorporates the specified test cases and follows the problem statement's guidelines to calculate the required sum of squares for odd numbers while disregarding negative or non-integer numbers.
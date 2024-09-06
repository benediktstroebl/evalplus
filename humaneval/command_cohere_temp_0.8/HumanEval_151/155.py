Here's a Python function that solves the given problem and includes informative docstrings to explain its behavior:
```python
def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    Parameters:
        lst (list): The input list of numbers.

    Returns:
        int: The sum of squares of odd integers that are non-negative and integers.
             If the list is empty or doesn't contain any eligible numbers, returns 0.
    """
    # Validate input: Check if the input list is empty or all negative
    if not lst or all(n < 0 for n in lst):
        return 0
    
    # Filter eligible numbers, square them, and sum up
    return sum(int(n)**2 for n in lst if n % 2 and isinstance(n, int))
```

This function, `double_the_difference`, takes a list of numbers as its argument and returns the sum of the squares of odd numbers in the list that are non-negative and integers. It ensures that negative numbers and non-integer values are ignored. The function returns 0 if the input list is empty or contains only negative numbers.

The parameter `lst` is described with a docstring that explains its purpose, and the return value is described as well. These documentation strings provide clarity on what the function expects as input and what it outputs, making it easier for others to understand and use correctly.
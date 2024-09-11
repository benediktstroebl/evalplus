```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list lst are below threshold threshold.
    
    Args:
        lst (list): A list of numbers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below the threshold, False otherwise.
    """
    return all(num < threshold for num in lst)


# Example usage:
print(below_threshold([1, 2, 4, 10], 100))   # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))    # Expected output: False
```

### Explanation:

*   The function `below_threshold` takes two parameters: `lst` (a list of numbers) and `threshold` (an integer).
*   It uses the built-in `all()` function in combination with a generator expression to check if all numbers in the list are below the threshold.
*   The `all()` function returns `True` if all elements of the iterable (in this case, the generator expression) are true.
*   The generator expression `(num < threshold for num in lst)` generates a sequence of boolean values, where each value is the result of the comparison `num < threshold` for a number `num` in the list.

### Additional Notes:

*   In Python, it's more common to use the `all()` function with a generator expression instead of a list comprehension.
*   Using a generator expression avoids creating an intermediate list, which can be more memory-efficient for large lists.
*   The function name `below_threshold` clearly indicates the function's purpose and parameters.
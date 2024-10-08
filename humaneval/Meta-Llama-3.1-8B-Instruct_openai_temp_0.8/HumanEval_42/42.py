### Increment List Elements
```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        l (list): The input list of integers.

    Returns:
        list: The list with elements incremented by 1.

    Examples:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]

# Example usage:
numbers = [1, 2, 3]
result = incr_list(numbers)
print("Original List:", numbers)
print("Incremented List:", result)

numbers = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(numbers)
print("\nOriginal List:", numbers)
print("Incremented List:", result)
```

This script uses a list comprehension to create a new list where each element is incremented by 1. The original list remains unchanged. The example usage demonstrates the function's behavior with two different input lists.
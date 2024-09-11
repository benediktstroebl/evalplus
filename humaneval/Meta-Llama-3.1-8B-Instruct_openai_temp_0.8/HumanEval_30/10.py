```python
def get_positive(numbers: list):
    """
    Return only positive numbers in the list.
    
    Args:
        numbers (list): A list of numbers.
    
    Returns:
        list: A list of positive numbers.
    """
    return [num for num in numbers if num > 0]


# Example usage:
print(get_positive([-1, 2, -4, 5, 6]))  # Expected output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: [5, 3, 2, 3, 9, 123, 1]
```

In this script, we define a function `get_positive` that uses a list comprehension to filter out non-positive numbers from the input list. The list comprehension iterates over each number in the input list and includes it in the output list only if it is greater than zero.
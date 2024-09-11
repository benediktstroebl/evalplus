```python
def get_positive(numbers: list):
    """
    Return only positive numbers in the list.

    Args:
        numbers (list): A list of numbers.

    Returns:
        list: A list of positive numbers from the input list.

    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]

# Example usage:
numbers = [-1, 2, -4, 5, 6]
positive_numbers = get_positive(numbers)
print(positive_numbers)  # Output: [2, 5, 6]
```

This script uses a list comprehension to create a new list that includes only the positive numbers from the input list. It iterates over each number in the input list and includes it in the new list only if the number is greater than zero. The result is then printed to the console. 

You can also use `filter()` function with `lambda` function to solve the same problem:

```python
def get_positive(numbers: list):
    return list(filter(lambda num: num > 0, numbers))
```
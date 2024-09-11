```markdown
### Solution to the Problem

Below is a Python script that defines a function `get_positive` to return only positive numbers from a given list.

```python
def get_positive(numbers: list) -> list:
    """
    Return only positive numbers in the list.

    Args:
        numbers (list): A list of numbers.

    Returns:
        list: A list of positive numbers.

    Example:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]

# Example usage
print(get_positive([-1, 2, -4, 5, 6]))
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
```

### Explanation

This script defines a function `get_positive` that uses list comprehension to filter out non-positive numbers from the input list. The condition `num > 0` is used to check if a number is positive. The function returns a new list containing only the positive numbers.

### Running the Script

Save this script to a file (e.g., `get_positive.py`) and run it using Python (e.g., `python get_positive.py`). You can also copy and paste the script into a Python interpreter or an IDE for execution.
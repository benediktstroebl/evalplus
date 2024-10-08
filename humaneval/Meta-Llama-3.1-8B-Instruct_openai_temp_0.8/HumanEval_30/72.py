### Python Script to Filter Positive Numbers in a List

Here's a simple Python script that defines a function `get_positive` to filter out positive numbers from a given list:

```markdown
### Positive Numbers Filter Function
```python
def get_positive(l: list):
    """
    Return only positive numbers in the list.
    
    Args:
        l (list): A list of integers.
    
    Returns:
        list: A new list containing only positive integers from the input list.
    
    Example:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in l if num > 0]

# Test the function
print(get_positive([-1, 2, -4, 5, 6]))  # Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: [5, 3, 2, 3, 9, 123, 1]
```

This script uses list comprehension to create a new list containing only the numbers from the input list that are greater than 0. The result is then printed to the console.
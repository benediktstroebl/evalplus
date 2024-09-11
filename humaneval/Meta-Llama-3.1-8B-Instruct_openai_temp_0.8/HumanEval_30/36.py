Here's a simple Python function to solve the problem:

```markdown
### get_positive Function
#### Returns a list of positive numbers from the input list

```python
def get_positive(numbers: list):
    """
    Return only positive numbers in the list.
    
    Args:
        numbers (list): A list of numbers.
    
    Returns:
        list: A list of positive numbers.
    
    Examples:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]
```

### Usage
You can use this function to filter a list of numbers and get only the positive ones.

```python
numbers = [-1, 2, -4, 5, 6]
positive_numbers = get_positive(numbers)
print(positive_numbers)  # Output: [2, 5, 6]
```

This function uses a list comprehension to create a new list that includes only the numbers from the input list that are greater than zero.
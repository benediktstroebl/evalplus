### Filter Positive Numbers from a List

Below is a Python function that filters out only the positive numbers from a given list. This function uses Python's built-in list comprehension feature to create a new list containing only positive numbers.

```markdown
### Code
```python
def get_positive(num_list: list):
    """
    Return only positive numbers in the list.

    Args:
    num_list (list): A list containing integers or floats.

    Returns:
    list: A list containing only positive numbers from the input list.

    Examples:
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in num_list if num > 0]

# Example usage:
numbers = [-1, 2, -4, 5, 6]
positive_numbers = get_positive(numbers)
print(positive_numbers)  # Output: [2, 5, 6]
```

### Explanation

- This function `get_positive(num_list: list)` takes a list of integers or floats as input.
- It uses a list comprehension to iterate over each number in the input list.
- For each number, it checks if the number is greater than 0 (`num > 0`).
- If the number is positive, it includes it in the new list.
- The function returns the new list containing only positive numbers.
- In the example usage, we create a list `numbers` and pass it to the `get_positive` function. The result is stored in the `positive_numbers` variable and printed to the console.
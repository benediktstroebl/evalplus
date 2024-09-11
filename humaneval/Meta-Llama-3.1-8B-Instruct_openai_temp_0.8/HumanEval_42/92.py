### Increment List Elements
#### Python Script

```markdown
# Define a function to increment elements in a list
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        l (list): A list of integers

    Returns:
        list: The input list with elements incremented by 1

    Examples:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]

# Example usage:
print(incr_list([1, 2, 3]))  # Output: [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

### How it Works

1. The function `incr_list` takes a list of integers `l` as input.
2. It uses a list comprehension to create a new list where each element `x` is incremented by 1.
3. The resulting list is returned.

### Note

This script uses a list comprehension for a concise and efficient solution. It also includes docstrings and example usage to demonstrate the function's behavior.
Here's a Python script that defines a function called `incr_list` to increment each element in the input list by 1.

```markdown
### Increment List Elements
#### Code
```python
def incr_list(l: list) -> list:
    """Return list with elements incremented by 1.

    Args:
    l (list): The input list.

    Returns:
    list: The list with elements incremented by 1.

    Examples:
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]
```

#### Usage
```python
# Create a sample list
numbers = [1, 2, 3]

# Increment list elements
incremented_numbers = incr_list(numbers)

# Print the incremented list
print(incremented_numbers)

# Output:
# [2, 3, 4]
```
This script uses list comprehension to create a new list where each element is incremented by 1. The function takes an input list, increments each element, and returns the new list. The example usage demonstrates how to create a sample list, increment its elements, and print the result.
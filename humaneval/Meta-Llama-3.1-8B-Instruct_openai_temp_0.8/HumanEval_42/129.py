### Solution

Here's a self-contained Python script that defines and tests the `incr_list` function:

```markdown
### incr_list Function
#### Increment each element in a list by 1

```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        l (list): Input list of numbers.

    Returns:
        list: List with all elements incremented by 1.

    Examples:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]
```

### Testing the Function

```python
import doctest

# Run tests
doctest.testmod()
```

### Example Usage

```python
# Create a test list
test_list = [1, 2, 3]

# Increment the list
incremented_list = incr_list(test_list)

# Print the result
print(incremented_list)  # Output: [2, 3, 4]
```

### Explanation

The `incr_list` function uses a list comprehension to create a new list with each element incremented by 1. This approach is more efficient and Pythonic than using a for loop to iterate over the input list. The `doctest` module is used to run the test cases provided in the docstring.
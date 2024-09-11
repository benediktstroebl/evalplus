```python
def incr_list(l: list):
    """Return list with elements incremented by 1.

    Args:
        l (list): A list of integers.

    Returns:
        list: A new list with elements incremented by 1.

    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [i + 1 for i in l]
```

In this script, I used Python's list comprehension feature to create a new list where each element is the corresponding element in the original list incremented by 1. This approach is efficient and concise.

**Example use case:**

```python
# Create a list of integers
numbers = [1, 2, 3, 4, 5]

# Increment each number by 1 using the incr_list function
incremented_numbers = incr_list(numbers)
print(incremented_numbers)
# Output: [2, 3, 4, 5, 6]
```
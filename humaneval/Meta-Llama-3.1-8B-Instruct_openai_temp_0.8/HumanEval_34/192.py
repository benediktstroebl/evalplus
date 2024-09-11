### Unique Elements in a List

Below is a Python function that solves the problem of finding unique elements in a list.

```markdown
### Code
```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

### Example Usage
if __name__ == "__main__":
    # Test case with a list of numbers
    numbers = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    unique_numbers = unique(numbers)
    print(unique_numbers)

    # Test case with a list of strings
    strings = ['apple', 'banana', 'apple', 'orange', 'banana']
    unique_strings = unique(strings)
    print(unique_strings)
```

This script defines a function `unique(l)` that takes a list `l` as input and returns a sorted list of unique elements. It uses the built-in `set()` function to remove duplicates and then sorts the resulting set using the `sorted()` function.

The example usage demonstrates how to use the `unique()` function with both a list of numbers and a list of strings. The output will be a sorted list of unique elements.

### How it Works
1. `set(l)` removes duplicates from the list by converting it into a set.
2. `sorted(set(l))` sorts the unique elements in ascending order.

### Notes
- This implementation assumes that the input list can be converted to a set (i.e., it contains only hashable elements).
- This function returns a new list and does not modify the original list.
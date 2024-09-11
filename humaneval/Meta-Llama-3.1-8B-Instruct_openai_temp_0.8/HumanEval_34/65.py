```python
def unique(nums: list) -> list:
    """Return sorted unique elements in a list

    Args:
        nums (list): Input list of numbers

    Returns:
        list: Sorted list of unique numbers

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(nums))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

In this script, we use the built-in Python functions `set` to remove duplicates and `sorted` to sort the resulting list. This is a concise and efficient way to solve the problem. The `set` function works by automatically removing any duplicate elements, leaving us with a collection of unique elements. We then pass this set to the `sorted` function to get a sorted list of unique numbers.
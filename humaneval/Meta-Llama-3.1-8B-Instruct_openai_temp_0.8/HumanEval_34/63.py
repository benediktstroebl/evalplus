### Unique Elements in a List
Here's a Python script that implements the `unique` function as per the provided specification:

```markdown
### unique.py

```python
def unique(l: list):
    """Return sorted unique elements in a list

    Args:
        l (list): Input list of elements

    Returns:
        list: Sorted list of unique elements

    Example:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

### Explanation:

*   The `unique` function takes a list `l` as input and returns a sorted list of unique elements.
*   We use the built-in `set` function to remove duplicates, and then convert it back to a list using the `list` function.
*   Finally, we sort the list using the `sorted` function and return the result.
*   In the example usage, we demonstrate how to use the `unique` function and print the result.

### Running the Script:

1.  Save the script as `unique.py`.
2.  Run the script using Python: `python unique.py`
3.  You should see the sorted list of unique elements printed to the console.
### Unique Elements in a List
#### Python Script to Return Sorted Unique Elements

Here is a self-contained Python script that uses a set to remove duplicates and the built-in `sorted` function to sort the unique elements:

```markdown
### Code

```python
def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

### Explanation

*   The `unique` function takes a list `l` as input.
*   It converts the list to a set using `set(l)`, which automatically removes duplicates since sets only contain unique elements.
*   The `sorted` function is then used to sort the unique elements in ascending order.
*   The sorted unique elements are returned by the function.
*   In the example usage, we call the `unique` function with the provided list and print the result.
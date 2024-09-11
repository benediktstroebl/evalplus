### Unique Elements in a List
#### Self-Contained Python Script
```markdown
```python
def unique(l: list):
    """
    Returns sorted unique elements in a list.
    
    Args:
    l (list): Input list containing elements to be processed.
    
    Returns:
    list: Sorted list of unique elements.
    
    Example:
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(set(l))

# Example usage
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

### Explanation
*   We define a function `unique(l: list)` that takes a list `l` as input.
*   Inside the function, we use the built-in `set()` function, which removes duplicate elements from the list. It returns a set, which is an unordered collection of unique elements.
*   To sort the resulting set, we use the `sorted()` function, which returns a new sorted list from the elements of any sequence.
*   Finally, we provide an example of how to use the `unique()` function with the input list `[5, 3, 5, 2, 3, 3, 9, 0, 123]`.
*   In the example usage section, the sorted list of unique elements `[0, 2, 3, 5, 9, 123]` is printed to the console.
```
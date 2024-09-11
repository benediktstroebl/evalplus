```python
def unique(l: list):
    """Return sorted unique elements in a list
    
    Args:
        l (list): Input list
    Returns:
        list: Sorted unique elements in the list
    """
    return sorted(set(l))

# Example usage:
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

Explanation:

*   The `unique` function takes a list `l` as input.
*   The `set(l)` expression converts the list to a set, which automatically removes any duplicate elements.
*   The `sorted` function then sorts the set of unique elements in ascending order.
*   The sorted unique elements are returned by the function.
*   In the example usage, we call the `unique` function with a sample list and print the result.
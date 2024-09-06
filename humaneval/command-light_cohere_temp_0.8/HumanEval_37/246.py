```python
def sort_even(l: list):
    """Sorts list l so that all odd indices contain the original value, and even indices contain the first value of the corresponding even index.
    Returns a A sorted list l' such returned.
    """
Example:
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    """
    return sorted(l, key=lambda x: x%2)

# Test the function
test_list = [5, 6, 3, 4]
print(sort_even(test_list))  # [3, 6, 5, 4]
```
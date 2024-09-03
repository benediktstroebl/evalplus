```python
def sort_array(arr):
    """
    Sort array of non-negative integers based on ones in binary representation.
    For same number of ones, sort by decimal value.
    """
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
```
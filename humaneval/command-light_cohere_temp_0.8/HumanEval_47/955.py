```python
def median(lst):
    """Return the median of the list lst."""
    if len(lst) == 0:
        return None
    mid = len(lst) // 2
    if lst[mid] > lst[len(lst) - 1 - mid]:
        return (lst[mid] + lst[len(lst) - 1 - mid]) / 2.0
   
   
    # Test cases
    assert median([3, 1, 2, 4, 5]) == 3.0
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    ```
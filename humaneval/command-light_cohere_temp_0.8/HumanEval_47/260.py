```python
def median(lst):
    """Return median of elements in the list lst"""
    n = len(lst)

    # Sort the list in ascending order
    lst.sort(key=lambda x: x)
    median = (lst[-1] + lst[0]) / 2

    # Verify median is in the right range
    assert median >= 1 and median <= len(lst)

    # Verify median is correct for all cases
    assert median == (
        lst[int(n / 2)] + lst[n - int(n / 2)]) / 2 if n % 2 == 1 else \
        lst[int((n + 1) / 2)] + lst[int((n - 1) / 2)]) / 2
    ```
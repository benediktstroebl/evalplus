```python
def median(lst):
    n = len(lst)
    if n <= 1:
        return lst[0]  # Return any element as median if list has 0 or 1 elements
    mid = n // 2
    left = lst[mid - 1]
    right = lst[mid]
    return (left + right) / 2 if n % 2 != 0 else left

# Test the function
# Want the median of [-10, 4, 6, 1000, 10, 20]
result = median([-10, 4, 6, 1000, 10, 20])
assert result == 15.0

```
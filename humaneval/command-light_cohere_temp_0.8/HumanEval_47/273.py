```python
def median(lst):
    if len(lst) == 0:
        return None
    
    mid = len(lst) // 2
    left = lst[mid - 1]
    right = lst[mid]
    return float(left + right) / 2 if left + right != float('inf') else None

# Test suite
assert median([3, 1, 2, 4, 5]) == 3.0
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([9, 8, 7]) == 7.0
assert median([21, 22, 23]) == (21 + 22) / 2
```
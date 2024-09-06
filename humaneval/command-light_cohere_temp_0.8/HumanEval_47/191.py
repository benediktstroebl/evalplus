```python
def median(lst):
    if len(lst) <= 1:
        return lst[0]
    mid = len(lst) // 2
    if lst[mid] > lst[mid + 1]:
        mid = (mid + 1)
    median_value = (lst[mid] + lst[mid + 1]) / 2
    return median_value

# Test cases
# Test 1:
median([3, 1, 2, 4, 5]) # Should return 3.5

# Test 2:
median([-10, 4, 6, 1000, 10, 20]) # Should return 15.0

# Test 3:
median([1, 2, 3, 4, 5]) # Should return 3.5

# Test 4:
median([10, -10, 20, 3, 4]) # Should return 15.0

# Test 5:
median([1000, 2, 1]) # Should return 1000
```
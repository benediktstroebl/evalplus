```python
def median(lst):
    n = len(lst)
    if n <= 1:
        return None  # Handle empty lists
    m = n // 2
    left, right = m - 1, m
    while left >= 0 and right < n:
        if lst[left] > lst[right]:
            left, right = left + 1, right
        mid = (left + right) // 2
        if lst[mid] == median([lst[left:mid + 1], lst[mid + 1:right + 1]]):
            return mid
        elif lst[mid] > median(lst[left:right + 1]):
            right = mid - 1
        else:
            left = mid + 1
    return None  # Handle ties or improperly sorted lists

# Test the median function
lst1 = [1, 2, 3, 4, 5]
assert median(lst1) == 3

lst2 = [-10, 4, 6, 1000, 10, 20]
assert median(lst2) == 5

lst3 = [10, 20, 10, 4, 3]
assert median(lst3) is None
```
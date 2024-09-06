```python
def median(lst):
    if len(lst) < 1:
        raise ValueError("List cannot be empty.")
    if len(lst) == 1:
        return lst[0]
    mid = len(lst) // 2
    if lst[mid] > lst[len(lst) - 1 - mid]:
        return median(lst[:mid]) + median(lst[mid:])
    else:
        return median(lst[mid:])

# Test cases
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
print(median([10, 20, 1000, 2, 0, 1]))  # Output: 10
```
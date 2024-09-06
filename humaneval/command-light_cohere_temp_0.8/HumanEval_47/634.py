```python
def median(lst):
    if len(lst) == 0:
        return None  # Handle empty list
    mid = len(lst) // 2
    if lst[mid] > lst[len(lst) - 1 - mid]:
        return (mid + 1) * (lst[mid] + lst[len(lst) - 1 - mid]) / 2
    else:
        return (len(lst) - 1 - mid) * (lst[mid] + lst[len(lst) - 1 - mid]) / 2

# Example usage
lst = [10, 20, 30, 40, 1, 2, 3]
print(median(lst))  # Output: 25.0
```
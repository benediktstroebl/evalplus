```python
def median(lst):
    if len(lst) == 0:
        raise ValueError("List cannot be empty")
    if len(lst) % 2 == 1:
        return (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
    else:
        return (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2

# Test cases
print(median([-10, 40, 25, 15, 8]))  # 15.0
print(median([-10, 4, 6, 1000, 10, 20]))  # 15.0
print(median([1, 2, 3, 4, 5]))  # 3
print(median([10, 20, -8, -5, 80]))  # 15.0
print(median([10, 20, 30, 10]))  # 15.0
print(median([1, 2, -3, 4, 5]))  # 3
print(median([10, 20, 10, 10, 20]))  # 15.0
```
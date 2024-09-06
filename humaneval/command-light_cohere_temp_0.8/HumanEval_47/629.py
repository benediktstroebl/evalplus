```python
def median(lst):
    if len(lst) <= 1:
        return lst[0]
    elif len(lst) % 2 == 0:
        return (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
    else:
        return lst[len(lst) // 2]

# Test cases
print(median([3, 1, 2, 4, 5]))  # Output: 3.5
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 10.5
print(median([4, -5, -4, -3]))  # Output: -4
```
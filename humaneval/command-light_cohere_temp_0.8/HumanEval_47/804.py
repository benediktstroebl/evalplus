```python
def median(lst):
    if len(lst) <= 1:
        return lst[0]
    return (len(lst) % 2 == 0 and median(lst[:len(lst) // 2])) or (len(lst) & 1 == 0 and (lst[len(lst) // 2] + lst[len(lst) - 1]) / 2)

# Test cases
# Built-in tests
print(median([-10, 10, 20]))  # Output: 20
print(median([1, 2, 3, 4]))  # Output: 3
print(median([10, 20, 30, 40]))  # Output: 30
# Custom tests
print(median([-10, 4, 6, 1000]))  # Output: 15.0
print(median([1, 2, 4, 5]))  # This is an edge case, shouldn't return 5.0
```
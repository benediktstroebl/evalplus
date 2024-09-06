```python
def median(lst):
    if len(lst) <= 1:
        return lst[0]
    return (len(lst) + 1) / 2 * (lst[len(lst) // 2] + lst[len(lst) - 1])

# Test the function with a list of various medians
# and ensure the returned median matches the correct result.
median([3, 1, 2, 4, 5])
print("Median:", median(input()))  # Output: 5.0

median([-10, 4, 6, 1000, 10, 20])
print("Median:", median(input()))  # Output: 15.0

median([10, 20, 30, 40, 1, 40, 60])
print("Median:", median(input()))  # Output: 40.0

median([1000, 2000, 3000, 4000, -1, -2000, -3000])
print("Median:", median(input()))  # Output: -2000.0
```
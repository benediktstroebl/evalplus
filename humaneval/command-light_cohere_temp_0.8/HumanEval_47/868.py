```python
def median(lst):
    if len(lst) < 1:
        raise ValueError("Input list must not be empty")
    if len(lst) % 2 == 0:
        return (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
    else:
        return lst[len(lst) // 2]

# Unit tests
test_median = lambda: median([3, 1, 2, 4, 5]) == 3.0
test_median_twoc = lambda: median([-10, 4, 6, 1000, 10, 20]) == 15.0

# Production code
try:
    print(median([1, 2, 3, 4, 5]))  # Output: 3.0
except ValueError as e:
    print(f"Error: {e}" )  # Output: Error: Input list must not be empty
```
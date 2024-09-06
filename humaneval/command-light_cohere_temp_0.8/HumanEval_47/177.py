```python
def median(lst):
    if len(lst) < 1:
        raise ValueError("Input list cannot be empty")
    if len(lst) % 2 == 0:
        return (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
    else:
        return lst[len(lst) // 2]

# Test the function with a list of numbers
test_median = [10, 20, 4, 6, 3, -10, 150]
result = median(test_median)
assert result == 5.0
```
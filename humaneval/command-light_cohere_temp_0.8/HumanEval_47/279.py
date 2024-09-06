```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[(n // 2) - 1] + lst[n // 2]) / 2
    else:
        return lst[n // 2]

# Test case 1
test_median = [4, 6, 2, 1]
assert median(test_median) == 2

# Test case 2
test_median = [4, 6, 2, 10]
assert median(test_median) == 4

# Test case 3
test_median = [10, 10, 10]
assert median(test_median) == 10

# Test case 4
test_median = [-10, 4, 6, 1000]
assert median(test_median) == 6

# Test case 5
test_median = [1000, 1000, 4, 6]
assert median(test_median) == 6
```
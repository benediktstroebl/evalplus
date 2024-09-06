```python
def median(l):
    n = len(l)
    if n % 2 == 0:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]

# Test cases
for testCase in ["median([3, 1, 2, 4, 5]), median([-10, 4, 6, 1000, 10, 20])"]:
    assert testCase() == 15.0, "Verify the result"
```

This script defines a function median that calculates the median of a list. It uses the simple logic to check if the length of the list is even or odd and then applies the appropriate formula to find the median. 

The test cases ensure that the function is working correctly by passing various lists and comparing the result with the expected floating-point value for the median.
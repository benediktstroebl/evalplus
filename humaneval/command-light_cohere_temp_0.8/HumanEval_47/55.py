```python
def median(l: list):
    n = len(l)
    if n % 2 == 1:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test cases
test_median = lambda: median([3, 1, 2, 4, 5])
should_pass = [test_median()] == [15.0,]
```
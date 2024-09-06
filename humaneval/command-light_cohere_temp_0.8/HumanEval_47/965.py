```python
def median(l: list):
    """Return median of elements in the list l.
    m = sorted(l)
    n = len(m)
    if n % 2 == 0:
        return (m[(n // 2) - 1] + m[n // 2]) / 2
    else:
        return m[(n // 2)]

# Test cases
test_median = [
    [(-10, 4, 6, 1000, 10, 20),
     (20, -100, 1000, -20),
     (1, 2, 3, 4, 5)],
	[0, 0.0]

def test_func(test_cases):
    for test_case in test_cases:
        for case, value in enumerate(test_case):
            assert median(test_case)[case] == value

test_median = test_func(test_median)  # Call function with test cases
```
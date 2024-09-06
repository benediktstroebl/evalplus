```python
def median(l: list):
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test the function
def test_median():
    input = [-10, 4, 6, 1000, 10, 20]
    expected = 15.0
    result = median(input)
    assert result == expected, f"expected {expected}, got {result}"

# Call the test function
test_median()
```
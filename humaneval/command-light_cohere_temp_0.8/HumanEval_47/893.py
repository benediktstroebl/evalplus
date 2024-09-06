```python
def median(l: list):
    n = len(l)
    if n % 2 == 0:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]

# Test the function
def test_median():
    # Example list for testing
    test_list = [3, 1, 2, 4, 5, 10, 20, -10, 6]
    result = median(test_list)
    assert result == 5.0, "Median is not calculated correctly!"

# Call the function and test it
test_median()
```
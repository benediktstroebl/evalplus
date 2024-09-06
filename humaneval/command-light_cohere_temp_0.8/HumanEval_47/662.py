```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2
    else:
        return lst[n // 2]

# Test the function
def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.0
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([1, 2, 4, 5]) == 5.0
    assert median([10, 20, 30, 40]) == 20.0
    assert median([1, 2, 3, 4, 5]) == 5.0

test_median()
```
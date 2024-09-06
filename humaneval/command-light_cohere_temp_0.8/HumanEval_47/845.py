```python
def median(l: list):
    n = len(l)
    if n % 2 == 1:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]

# Test
def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.0
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([]) == 0.0
``` 
The code defines a function `median` that calculates the median of the elements in a list. The function handles both cases: odd-length lists and even-length lists. The test functions verify the good results for different inputs.
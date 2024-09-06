```python
def median(lst):
    n = len(lst)
    if n <= 1:
        return None
    mid = n // 2
    left = median(lst[:mid])
    right = median(lst[mid:])
    return (left + right) / 2 if left is not None and right is not None else None

def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.0  #

test_median()
```
This code defines a median() function that calculates the median of a list of numbers. It then tests the requires that the median function is correctly implemented.
```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test cases
test_get_positive = [
    ()
    [[-1, 2, -4],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    [1, 2, 3, 4, 5, 6]
]

def test():
    assert get_positive([-1, 2, -4]) == [2, 4]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]
    assert get_positive([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5]
    assert len(get_positive([1, 2, -3, 4, 5, 6])) == 5
test_get_positive()
```
This code defines the function `get_positive`, which takes a list as input and returns a new list containing only the positive elements from the original list. It also includes a test cases, which verify the correctness of the `get_positive` function for different input scenarios.
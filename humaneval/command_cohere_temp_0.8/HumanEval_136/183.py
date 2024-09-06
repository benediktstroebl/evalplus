```python
def largest_smallest_integers(lst):
    positive = float('-inf')
    negative = float('inf')
    for n in lst:
        if n > 0:
            if n > positive:
                positive = n
        else:
            if n < negative:
                negative = n
    return (negative if negative != float('inf') else None,
            positive if positive != float('-inf') else None)
```

The `largest_smallest_integers` function iterates through the list, identifying the smallest positive integer and the largest negative integer. It uses `float('-inf')` and `float('inf')` to represent the minimum and maximum values respectively. By comparing values against these constants, it finds the desired integers. The function then returns a tuple containing the largest negative and smallest positive integers, or `None` if none are present. 

The following is a simple test suite that can be used to validate the functionality:
```python
def test_largest_smallest_integers():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([-1, -2, -3, -4, -5]) == (-5, None)
    assert largest_smallest_integers([1, 2, 3, 4, 5, -5, -4, -3, -2, -1]) == (-1, 1)
```

To run the tests, you can call the `test_largest_smallest_integers` function in your Python environment.
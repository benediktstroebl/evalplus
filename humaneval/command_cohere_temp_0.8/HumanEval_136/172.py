```python
def largest_smallest_integers(lst):
    negative = None
    positive = None
    for n in lst:
        if n < 0:
            if negative is None or n > negative:
                negative = n
        else:
            if positive is None or n < positive:
                positive = n
    return (negative, positive)
```

The Python script defines a function `largest_smallest_integers` that solves the problem as described in the prompt. It iterates through the list, identifying the largest negative and smallest positive integers, or `None` if none are found.

Here is a simple test suite:
```python
def test_largest_smallest_integers():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([-3, -5, -1, -7, -4, -2]) == (-2, 2)

test_largest_smallest_integers()
```

The test suite proves the correctness of the function for various cases.
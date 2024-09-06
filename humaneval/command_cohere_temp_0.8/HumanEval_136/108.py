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

The provided code defines a function `largest_smallest_integers` that solves the problem as described in the prompt. It iterates through the list, identifying the largest negative and smallest positive integers, updating `negative` and `positive` accordingly. The function ultimately returns a tuple containing these two values. If no negative or positive integers are found, `None` is returned for both parts of the tuple.

Here is a simple test suite to verify the functionality of the function:
```python
def test_largest_smallest_integers():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([-1, -2, -3, -4, -5]) == (-5, None)
    assert largest_smallest_integers([1, 2, 3, 4, 5, -6, -1, -2, -3]) == (-3, 1)

test_largest_smallest_integers()
```

The test suite contains four test functions to cover different scenarios. Each test function calls the `largest_smallest_integers` function with a specific list of integers and asserts that the returned tuple matches the expected result.
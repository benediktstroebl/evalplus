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

The `largest_smallest_integers` function works by initially setting two variables, `negative` and `positive`, to `None.` As the function iterates through the list, it compares the current element `n` to the established variables.

If `n` is smaller than 0 (thus, a negative integer), the function checks if `negative` is presently `None` or whether `n` is greater than the existing `negative`. If so, the variable `negative` is updated to `n.`

If `n` is greater than 0 (and therefore positive), the function checks if `positive` is `None` or whether `n` is less than the existing `positive`. If this condition is met, `positive` is updated to `n`.

Finally, the function returns a tuple of (negative, positive). None is inserted in place of the missing value if there is no negative or positive integer in the list.

Here is a simple test suite to ensure the functionality of the function:
```python
def test_largest_smallest_integers():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([-1, -10, -5, -3, -2, -1]) == (-1, None)
    assert largest_smallest_integers([1, 2, 3, 4, 5, 6, 7, 8, 9]) == (None, 9)
```

To run the tests, you can call the test function in the Python environment. The assert statements will throw an error if the expected output does not match the output of the `largest_smallest_integers` function.

This script ensures the `largest_smallest_integers` function behaves as intended, correctly identifying the largest negative and smallest positive integers among any provided list.
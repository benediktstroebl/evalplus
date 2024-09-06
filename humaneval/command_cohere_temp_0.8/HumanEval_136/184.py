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

The Python script defines a function `largest_smallest_integers` that solves the problem as described in the prompt. It iterates through the list, identifying the largest negative and smallest positive integers, updating `negative` and `positive` accordingly. The function ultimately returns a tuple containing these two values. If no negative or positive integers are found, `None` is returned for both components of the tuple.

Here is a simple test suite to verify the functionality of the code:
```python
def test_largest_smallest_integers():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([-3, -5, -1, -7, -4, -2]) == (-1, -2)
    assert largest_smallest_integers([1, 2, 3, 4, 5, -8, -7, 7, 8]) == (-8, 8)

test_largest_smallest_integers()
```

The test suite includes various test cases to validate the function's behavior and ensure it aligns with the problem statement. You can use the `test_largest_smallest_integers()` function to verify the correctness of the provided solution.
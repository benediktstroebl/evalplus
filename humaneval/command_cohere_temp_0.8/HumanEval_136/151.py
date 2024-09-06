```python
def largest_smallest_integers(lst):
    positive = None
    negative = None
    for n in lst:
        if n > 0:
            if positive is None or n > positive:
                positive = n
        elif n < 0:
            if negative is None or n < negative:
                negative = n
    return (negative, positive)
```

The `largest_smallest_integers` function iterates through the list of integers and identifies the largest negative integer and the smallest positive integer. The function compares these values and returns them, or `None` if no negative or positive integers are present.

Here is a simple test suite:
```python
def test_largest_smallest_integers():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (7, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
```

Run using:
```bash
python -m unittest test_largest_smallest_integers
``` 

This would verify that the function behaves as described in the problem statement.
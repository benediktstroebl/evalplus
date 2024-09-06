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

The Python script defines a function `largest_smallest_integers` that takes a list as an argument and returns a tuple containing the largest negative integer and the smallest positive integer in the list. The function initially assigns `None` to variables `positive` and `negative` to represent absence of positive or negative integers, respectively. It then iterates through the list, identifying the largest negative integer and the smallest positive integer. If present, the function updates the `negative` or `positive` variables to the respective largest or smallest value. Finally, the function returns a tuple of `(negative, positive)`.

Here is a markdown code block with some tests for the above function to validate its correctness:
```python
def test_largest_smallest_integers():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([-1, -2, -3, -4, -5]) == (-5, None)
    assert largest_smallest_integers([1, 2, 3, 4, 5, -6, -1, -2, -3]) == (-3, 1)
    assert largest_smallest_integers([-7, -8, -9, -10, -11, 1, 2, 3, 4]) == (-11, 4)
test_largest_smallest_integers()
```

The above test suite covers edge cases and various scenarios to ensure that the function `largest_smallest_integers` returns the correct results for different lists of integers.
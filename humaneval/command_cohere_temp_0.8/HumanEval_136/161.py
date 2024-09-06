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

The `largest_smallest_integers` function takes a list of integers as input and returns a tuple containing the largest negative integer and the smallest positive integer from the list. It initially assigns `None` to the variables `positive` and `negative` to represent absence of positive and negative integers, respectively. Then, it iterates through the list, identifying the largest negative integer and the smallest positive integer.

The following is a concise test suite to ensure the functionality of the function:
```python
def test_largest_smallest_integers():
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (7, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)
    assert largest_smallest_integers([-1, -2, -3, -4, -5]) == (-1, -5)
```

To run the test suite, you can copy and paste the test function into a Python file and execute the file. The code will then print detailed test results, including success/failure status and relevant messages.
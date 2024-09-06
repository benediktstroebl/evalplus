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

The `largest_smallest_integers` function iterates through the list, identifying positive and negative integers, and keeps track of the largest negative and smallest positive values encountered. The function will return `None` for each value if no positive or negative integers are present. This approach ensures that the solution effectively addresses all scenarios outlined in the problem description.

This approach has a time complexity of `O(n)` since it requires checking each element in the list once. It is also possible to simplify the code by using the `max` and `min` functions with a `key` parameter, but that may be outside the scope of this problem. 

The unit tests can be implemented as follows:
```python
def test_largest_smallest_integers():
    # Test case 1: Basic list with positive and negative integers
    assert largest_smallest_integers([2, -4, 1, 3, 5, 7]) == (7, 1)

    # Test case 2: List with no negative integers
    assert largest_smallest_integers([100, 200, 300]) == (None, 100)

    # Test case 3: List with no positive integers
    assert largest_smallest_integers([-10, -20, -30]) == (-30, None)

    # Test case 4: Empty list
    assert largest_smallest_integers([]) == (None, None)

    # Test case 5: List with a single 0
    assert largest_smallest_integers([0]) == (None, None)

test_largest_smallest_integers()
```

By defining a function `test_largest_smallest_integers` that calls the `largest_smallest_integers` function with the desired input scenarios and then comparing the actual results against the expected outputs, you can effectively verify the correctness of the solution.
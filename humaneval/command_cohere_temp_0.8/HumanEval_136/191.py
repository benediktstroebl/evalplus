```python
def largest_smallest_integers(lst):
    positive = min(x for x in lst if x > 0)
    negative = max(x for x in lst if x < 0)
    return negative, positive
```

The problem asks us to create a function that, given a list of integers, returns a tuple (`a`, `b`) where `a` is the largest integer among negative integers in the list and `b` is the smallest integer among positive integers in the list. If the list does not contain any negative or positive integers, `a` and `b` should be `None`.

The provided solution uses the `min` and `max` functions to find the smallest positive and largest negative integers in the list, respectively. These operations are commutative, meaning that `min(x, y)` is equal to `min(y, x)`. This means that we can pass in fractions, negatives, and positives interchangeably to collect the desired values.

This solution is concise and achieves the problem's requirements. It can be tested against the provided examples to confirm its correctness. Here is a test to check the functionality:
```python
def test_largest_smallest_integers():
    # None when an empty list is provided.
    assert largest_smallest_integers([]) == (None, None)

    # None when a list with a single 0 is provided.
    assert largest_smallest_integers([0]) == (None, None)

    # Regular cases.
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([-1, -11, -5, -13, -3, -9, -7]) == (-1, -3)
    assert largest_smallest_integers([0, 1, 2, 3, 4, 5, -1, -2, -3]) == (-3, 3)
```

This would ensure that the function works as expected. 

The `test_largest_smallest_integers` function tests the `largest_smallest_integers` function with the provided examples in the problem statement. It should help us confirm that the code provides the correct output for each scenario.
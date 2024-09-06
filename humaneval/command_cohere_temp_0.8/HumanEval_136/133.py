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

The `largest_smallest_integers` function iterates through the list of integers, identifying the largest negative and smallest positive integers. The function simplifies the logic by using `None` initialization and updation, ensuring that only the strongest or weakest integer is retained at each step. 

Here is a simple test suite that can be used to validate the functionality of the script:
```python
def test_largest_smallest_integers():
    # Basic Test Cases
    assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0]) == (None, None)

    # Edge Cases
    assert largest_smallest_integers([1, -3, 2, 4, -1, 5]) == (-1, 1)
    assert largest_smallest_integers([-2, -1, 0, 1]) == (-2, 1)

    # No Positive or Negative Numbers
    assert largest_smallest_integers([0, 0]) == (None, None)
    assert largest_smallest_integers([2, 2, 2]) == (None, 2)

test_largest_smallest_integers()
```

The test suite covers multiple scenarios, including basic tests, edge cases, and cases where the list contains no positive or negative integers. 

To run the test suite, save the Python script in a file, navigate to its directory, and run the test function. 

Ensure that your code passes the test suite before submission or usage, as it guarantees the function's correctness in various situations. 

This way, you can confidently use the `largest_smallest_integers` function to solve the problem efficiently.
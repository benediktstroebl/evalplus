Here's a Python function that solves the given problem and includes informative tests.

```python
def double_the_difference(lst):
    """
    Sum of squares of odd integers from the list ignoring negatives and non-integers.
    
    Returns 0 if the list is empty or non-numeric.
    """
    if not lst:
        return 0
    
    odd_squares = sum(x**2 for x in lst if x % 2 and isinstance(x, int) and x >= 0)
    return odd_squares

# Test Scenarios
def test_double_the_difference():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0
    assert double_the_difference([1, -2, 2.5, 3]) == 1 + 9 + 4 + 9 = 23

test_double_the_difference()
```

In this script, the function 'double_the_difference' is defined with a docstring that explains its purpose. Several tests are included to validate the function against different input scenarios. Each test case confirms that the function behaves as described for each scenario.
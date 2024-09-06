Here's a Python function that solves the given problem and includes informative tests.

```python
def double_the_difference(lst):
    """
    Sum of squares of odd integers from the list ignoring negatives and non-integers.
    
    Returns 0 if the list is empty or only contains negatives, non-integers, or zeros.
    """
    if not lst or all(x <= 0 or not isinstance(x, int) or x % 2 == 0 for x in lst):
        return 0
    
    return sum(x**2 for x in lst if x % 2 != 0)

def test_double_the_difference():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0
    assert double_the_difference([-1, 0, 1, 2, 3]) == 1 + 9 + 4 + 16 + 9 = 41
    assert double_the_difference([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 321

if __name__ == "__main__":
    test_double_the_difference()
```

In this script, the `double_the_difference` function handles the core logic, while the `test_double_the_difference` function provides a variety of test cases, including edge cases, to validate the behavior of the function. If all tests pass when executing the script, it indicates the function works as expected.
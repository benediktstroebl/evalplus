Here's a Python script with a self-contained function that solves the problem and includes relevant tests to verify its correctness:
```python
def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    """
    result = 0
    for num in lst:
        if isinstance(num, int) and num % 2 != 0 and num >= 0:
            result += num ** 2
    return result

# Test cases
def test_double_the_difference():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0
    assert double_the_difference([2, 4, 6, 8]) == 50
    assert double_the_difference([-2, -4, -6, -8]) == 0
    assert double_the_difference([]) == 0

# Execute the tests
test_double_the_difference()
```

In this script, the `double_the_difference` function iterates through each number in the input list. It checks if each number is an integer, odd, and non-negative before adding its square to the result. The test cases cover different scenarios to verify the function's behavior for various input lists.

After executing the script, the tests are automatically run, and any failures or errors will be reported. If all tests pass, it indicates that the function `double_the_difference` is correctly solving the problem.
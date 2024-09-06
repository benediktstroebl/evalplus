Here's a Python function that solves the given problem and includes informative tests.

```python
def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    """
    result = 0
    for num in lst:
        if num % 2 != 0 and num >= 0 and isinstance(num, int):
            result += num ** 2
    return result

def test_double_the_difference():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0
    assert double_the_difference([2, 4, 6, 8]) == 2 + 16 + 36 + 64
    assert double_the_difference([-2, -4, -6, -8]) == 0
    assert double_the_difference([]) == 0

if __name__ == "__main__":
    test_double_the_difference()
```

In this script, the `double_the_difference` function iterates through the list, squares each odd number that is a non-negative integer, and returns the sum of those squares. The `test_double_the_difference` function provides a few test cases to validate the behavior of the `double_the_difference` function.

The `if __name__ == "__main__":` block runs the test function when the script is executed directly, ensuring that the function behaves as expected.
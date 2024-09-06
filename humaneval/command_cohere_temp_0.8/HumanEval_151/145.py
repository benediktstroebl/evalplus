Here's a Python function that solves the given problem and includes informative tests.

```python
def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    """
    result = 0
    for num in lst:
        if num % 2 == 1 and isinstance(num, int) and num >= 0:
            result += num ** 2
    return result

def test_double_the_difference():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0
    assert double_the_difference([1, -1, 2, 3, -4, 5, -2]) == 25

if __name__ == "__main__":
    test_double_the_difference()
```

In this script, the `double_the_difference` function iterates through the list, checking for odd integers that are also positive integers. It then squares these numbers and sums them. The `test_double_the_difference` function provides tests for various cases, ensuring that the function's behaviour matches the problem's description. Finally, executing the script with `if __name__ == "__main__":` runs the tests.
Here's a Python function that solves the given problem and includes corresponding tests to verify its correctness:
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

# Test cases
def test_double_the_difference():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0
    assert double_the_difference([2, 4, 6, 8]) == 200
    assert double_the_difference([-2, -4, 6, -8]) == 0
    assert double_the_difference([]) == 0

if __name__ == "__main__":
    test_double_the_difference()
```

In this script, the `double_the_difference` function iterates through the list and calculates the sum of squares for odd integers that are positive and integers, as per the problem's instructions. The test cases ensure that the function produces the expected results for various input scenarios.
Here's a Python function that solves the given problem and includes informative tests.

```python
def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    """
    result = 0
    for n in lst:
        if isinstance(n, int) and n > 0:
            if n % 2 == 1:
                result += n ** 2
    return result

def test_double_the_difference():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0
    assert double_the_difference([1, -1, 2, 3, -4, 5, 6]) == 1 + 25 + 9 + 9 + 4 + 25 + 36 = 125
    assert double_the_difference([]) == 0

if __name__ == "__main__":
    test_double_the_difference()
```

In this script, the `double_the_difference` function iterates through the list, squares odd positive integers, and sums them. The `test_double_the_difference` function provides a few test cases to validate the behavior of the `double_the_difference` function. 

The `if __name__ == "__main__":` block ensures that the test suite runs when the script is executed directly but not when it's imported as a module, thereby preserving resources and optimizing runtime.
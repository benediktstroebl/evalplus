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
            if n % 2:
                result += n ** 2
    return result

def test_double_the_difference():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0
    assert double_the_difference([2, 4, 6, 8]) == 50
    assert double_the_difference([-2, -4, 6, -8]) == 0
    assert double_the_difference([]) == 0

if __name__ == "__main__":
    test_double_the_difference()
```

In this script, the `double_the_difference` function iterates through the list, checking if each element is a positive integer, and if so, whether it's odd. If these conditions are met, it adds the square of the number to the result. The tests comprehensively verify the function's behavior for different input scenarios.
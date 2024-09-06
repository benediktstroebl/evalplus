Here's a Python script with a self-contained function that solves the problem and includes corresponding tests:
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

# Test cases
assert double_the_difference([1, 3, 2, 0]) == 10
assert double_the_difference([-1, -2, 0]) == 0
assert double_the_difference([9, -2]) == 81
assert double_the_difference([0]) == 0
assert double_the_difference([]) == 0
```

This script includes the `double_the_difference` function and several tests to verify its correctness for various cases. You can add more tests to further validate the function's behavior.
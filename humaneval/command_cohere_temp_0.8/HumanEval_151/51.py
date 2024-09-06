Here's a Python script that includes a function `double_the_difference` that solves the problem statement and a set of tests to validate its correctness:
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
assert double_the_difference([1, 3, 2, 0]) == 10
assert double_the_difference([-1, -2, 0]) == 0
assert double_the_difference([9, -2]) == 81
assert double_the_difference([0]) == 0
assert double_the_difference([2, 4, 6, 8]) == 2 + 16 + 36 + 64
assert double_the_difference([-2, -4, -6, -8]) == 0
assert double_the_difference([]) == 0
```

In this script, the `double_the_difference` function iterates through each number in the input list. It checks if the number is odd, a non-negative integer, and adds its square to the result if so. The test suite covers various scenarios to ensure the function's correctness.
Here's a Python function that solves the given problem and includes corresponding tests to verify its correctness:
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
assert double_the_difference([1, 3, 2, 0]) == 10
assert double_the_difference([-1, -2, 0]) == 0
assert double_the_difference([9, -2]) == 81
assert double_the_difference([0]) == 0
assert double_the_difference([1, -1, 2, 3, -4, 5, -6]) == 1 + 25 + 9 + 1 + 25 + 1 = 81
assert double_the_difference([]) == 0
```

In this script, the `double_the_difference` function iterates through each number in the input list. It checks if each number is an integer, odd, and non-negative before adding its square to the result. The test cases ensure that the function produces the correct output for various inputs.
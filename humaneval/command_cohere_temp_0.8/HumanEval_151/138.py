Here's a Python script with a self-contained function that solves the problem and includes concise tests to verify its correctness:
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

# Tests
assert double_the_difference([1, 3, 2, 0]) == 10
assert double_the_difference([-1, -2, 0]) == 0
assert double_the_difference([9, -2]) == 81
assert double_the_difference([0]) == 0
assert double_the_difference([]) == 0
```

In this script, the `double_the_difference` function iterates through each number in the input list. If the number is odd, positive, and an integer, its square is added to the `result`. The corresponding tests ensure the function's correctness against different scenarios.
Here's a Python function that solves the given problem and includes concise test cases to verify its correctness:
```python
def double_the_difference(lst):
    odd_squares = sum(x ** 2 for x in lst if x % 2 and x >= 0 and isinstance(x, int))
    return 0 if not lst else odd_squares

# Test Cases
assert double_the_difference([1, 3, 2, 0]) == 10
assert double_the_difference([-1, -2, 0]) == 0
assert double_the_difference([9, -2]) == 81
assert double_the_difference([0]) == 0
assert double_the_difference([1, -2, 2.5, -1, 0]) == 1
assert double_the_difference([]) == 0
```

This script defines the `double_the_difference` function and uses assertion checks to verify its behavior against different input scenarios.

The function processes each number in the input list, checking if it's odd, non-negative, and an integer. If so, it calculates the square of the number and adds it to the running total. Finally, the function returns 0 if the input list is empty, or the total of odd squares otherwise.
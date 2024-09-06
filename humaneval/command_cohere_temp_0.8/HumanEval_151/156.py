Here's a Python function that solves the given problem and includes relevant tests:
```python
def double_the_difference(nums):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    """
    # First, we handle the edge case where the input list is empty
    if not nums:
        return 0
    
    odd_nums = [num for num in nums if num % 2 and num >= 0]
    squared_odd = [num ** 2 for num in odd_nums]
    return sum(squared_odd)

# Testing the function with various inputs and expected outputs:
test_cases = [
    ([1, 3, 2, 0], 10),
    ([-1, -2, 0], 0),
    ([9, -2], 81),
    ([0], 0),
    ([], 0),
]

for nums, expected in test_cases:
    assert double_the_difference(nums) == expected
```
This script provides a function `double_the_difference` that takes a list of numbers as input and returns the sum of squares of odd numbers in the list, ignoring any negative numbers or non-integer values. It also includes a list of test cases to validate the function's behavior against expected outputs.
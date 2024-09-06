Here's a Python function that solves the given problem and includes concise test cases to validate its correctness:
```python
def double_the_difference(lst):
    odd_sqrs = sum(x**2 for x in lst if x % 2 and x >= 0)
    return 0 if not lst else odd_sqrs

# Test Cases
assert double_the_difference([1, 3, 2, 0]) == 10
assert double_the_difference([-1, -2, 0]) == 0
assert double_the_difference([9, -2]) == 81
assert double_the_difference([0]) == 0
assert double_the_difference([1, -2, 7, 4, -3, 5, 6]) == 1 + 25 + 49 + 0 + 9 + 25 + 36 = 161
assert double_the_difference([]) == 0
```

The function `double_the_difference` uses a list comprehension to filter odd, non-negative integers from the input list and calculates their squares. The test cases ensure the function's behavior matches the specified conditions.
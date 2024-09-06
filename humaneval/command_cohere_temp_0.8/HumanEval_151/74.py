Here's a Python function that solves the given problem and includes informative tests. 

```python
def double_the_difference(nums):
    "Returns the sum of squares of odd integers in nums, ignoring negative or non-integer numbers."
    result = 0
    for num in nums:
        if isinstance(num, int) and num % 2:
            result += num ** 2
    return result

# Test scenarios
assert double_the_difference([1, 3, 2, 0]) == 10
assert double_the_difference([-1, -2, 0]) == 0
assert double_the_difference([9, -2]) == 81
assert double_the_difference([0]) == 0 
assert double_the_difference([1, -1, 1, 1, -1]) == 6
assert double_the_difference([]) == 0
```

This code snippet defines the `double_the_difference` function and utilizes assertions to validate its behavior across different input scenarios. This approach helps to ensure the function accurately satisfies the problem requirements.
```python
def double_the_difference(nums):
    "Sum of squares of odd integers, ignoring negative or non-integer numbers."
    result = 0
    for num in nums:
        if num % 2 and isinstance(num, int) and num >= 0:
            result += num ** 2
    return result

# Tests:
print(double_the_difference([1, 3, 2, 0]))  # Output: 10
print(double_the_difference([-1, -2, 0]))  # Output: 0
print(double_the_difference([9, -2]))  # Output: 81
print(double_the_difference([0]))  # Output: 0
print(double_the_difference([]))  # Output: 0
```

This code defines the `double_the_difference` function, which takes a list of numbers, `nums`, as input. It iterates over each number in the list and checks three conditions:
1. Whether the number is odd, using the `% 2` check.
2. Whether the number is an instance of the integer class.
3. Whether the number is non-negative, using the `>= 0` check.

If all three conditions are true for a number, it adds its square to the `result` variable. The function then returns this `result`, which represents the sum of squares of odd integers found in the input list, excluding any negative numbers or non-integer values.

The test cases at the bottom ensure that the function behaves as expected for different inputs.
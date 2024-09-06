Here's a Python script that includes a function to solve the given problem and a separate test script to validate its correctness:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        min_sum = min(n, min_sum + n)
        max_sum = max(n, max_sum + n)
    return min_sum + max_sum

# Testing the function
def test_min_sub_array_sum():
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    assert minSubArraySum([-1, -2, -3]) == -6
    assert minSubArraySum([0, 0, 0, 0]) == 0
    assert minSubArraySum([2, -1, 1, -1, 1, -1, 1]) == 0

# Run the tests
test_min_sub_array_sum()
```

In the above code, the `minSubArraySum` function calculates the minimum and maximum sum of the current subarray continuously while iterating through the input list. The example provided in the problem statement is also included in the test script to ensure the function behaves as expected.

To run the test, simply call the `test_min_sub_array_sum()` function. If all tests pass, it won't output anything. If any test fails, it will provide details about the failure.
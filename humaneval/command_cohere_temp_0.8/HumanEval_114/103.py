Here's a Python script that includes a function to solve the given problem and a separate test script to validate its correctness:
```python
def minSubArraySum(nums):
    if not nums:
        return 0
    
    min_sum = nums[0]
    max_sum = nums[0]
    
    for num in nums[1:]:
        min_sum = min(min_sum + num, num)
        max_sum = max(max_sum + num, num)
    
    return min(min_sum, max_sum)

# Test cases
tests = [
    [2, 3, 4, 1, 2, 4],
    [-1, -2, -3],
    [1, -1, -4, -1, -2, 1, -5, 3],
]

for test in tests:
    assert minSubArraySum(test) == 1
```

In the above code, the `minSubArraySum` function takes an array `nums` as input and iterates through it while keeping track of both the minimum and maximum sum encountered so far. This approach is often referred to as the "golden subarray" method. The function then returns the smaller of the two sums, which is the minimum sum of any non-empty sub-array.

The test script initializes a list of test cases, and for each test case, it calls the `minSubArraySum` function and compares the result with the expected output.
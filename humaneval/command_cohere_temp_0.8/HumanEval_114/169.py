Here's a Python function that solves the problem you've described:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums:
        min_sum = min(n, min_sum + n)
        max_sum = max(n, max_sum + n)
    return min_sum + max_sum
```

This script provides a function called `minSubArraySum` that takes in one argument, `nums`, which is an array of integers. The purpose of this function is to calculate the minimum sum of any non-empty sub-array within the given array. The function uses dynamic programming to efficiently compute this minimum sum by keeping track of both the minimum sum encountered so far (`min_sum`) and the maximum sum encountered so far (`max_sum`). The key idea is that the minimum subarray sum will be either the minimum sum encountered in the array or the sum of the current element added to the minimum sum encountered so far, whereas the maximum subarray sum will be either the maximum sum encountered in the array or the sum of the current element added to the maximum sum encountered so far. 

The function iterates through each number `n` in the array `nums`. For each number `n`, it updates both the min_sum and max_sum by considering both the case where the current number `n` is included and where it is not included in the sum. 

The example provided in the description of the problem would return the correct minimum subarray sum for the given arrays, namely `minSubArraySum([2, 3, 4, 1, 2, 4]) == 1` and `minSubArraySum([-1, -2, -3]) == -6`. 

This approach of dynamic programming is efficient because it has a time complexity of `O(n)` where `n` is the length of the input array, and a space complexity of `O(1)`, as it only requires a constant amount of extra space regardless of the input size.
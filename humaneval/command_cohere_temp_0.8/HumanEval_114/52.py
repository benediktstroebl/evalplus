Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        min_sum = min(min_sum + n, n)
        max_sum = max(max_sum + n, n)
    return min(min_sum, max_sum)
```

The function uses both a minimum and a maximum running sum to efficiently track the minimum sum of any subarray. When considering each new element `n`, the algorithm updates both the minimum running sum `min_sum` and the maximum running sum `max_sum`. The minimization is achieved by taking the lesser of the sum of the current element and the minimum running sum, and the maximum running sum. This step ensures the algorithm considers the minimum possible subarray sum that includes the current element. Similarly, the maximization is achieved by taking the greater of the sum of the current element and the maximum running sum, and the minimum running sum, which ensures the algorithm considers the maximum possible subarray sum that includes the current element. 

This approach has a time complexity of O(n) and uses constant space to track the running sums.
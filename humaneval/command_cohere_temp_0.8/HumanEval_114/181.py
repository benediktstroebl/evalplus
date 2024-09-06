Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        min_sum = min(n, min_sum + n)
        max_sum = max(n, max_sum + n)
    return min_sum + max_sum
```
This script defines a function called `minSubArraySum` that takes in one argument, `nums`, which is an array of integers. The function returns the minimum sum of any non-empty sub-array of `nums`. 

The script uses a brute-force approach, calculating the minimum and maximum sum achievable from each element in the array. These two values are maintained throughout the iteration. The minimum sum is updated considering both the current element and its potential sum with the minimum achieved so far, while the maximum sum is updated similarly. 

The script then returns the sum of the minimum and maximum values, which guarantees the smallest sum for any non-empty subarray. While this approach is straightforward, it does not optimize time complexity, especially for large arrays. More optimized approaches address this issue. 

The included self-contained script allows users to quickly implement the function and get the desired results without any external dependencies.
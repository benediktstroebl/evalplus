```python
def minSubArraySum(nums):
    min_sum = float('inf')
    nums.sort(reverse=True)
    for i in range(1, len(nums)):
        min_sum = min(min_sum, nums[i] + nums[i-1])
    return min_sum
```
This approach involves sorting the input array in a descending fashion. By doing this, consecutive elements in the array will be in order of decreasing magnitude. The minimum sum subarray must have the first element being the largest element in the array and the last element being the smallest element in the array.

Therefore, the sum of this subarray is `nums[0] + nums[-1]`, which is the minimum sum of any subarray. The function washes this sum to return the minimum sum of any non-empty subarray of `nums`. 

This approach's time complexity is O(Nlog(N)) due to the sorting step, which is necessary to optimize the analysis of the array.
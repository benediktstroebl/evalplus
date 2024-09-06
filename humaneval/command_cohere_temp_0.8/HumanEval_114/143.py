Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    cur_sum = 0
    min_sum = float('inf')
    for num in nums:
        cur_sum += num
        if cur_sum < 0:
            cur_sum = 0
        min_sum = min(min_sum, cur_sum)
    return min_sum
```

The function minSubArraySum takes an array of integers nums and returns the minimum sum of any non-empty sub-array of nums. The function initially sets the variable min_sum to a large value, ensuring that any valid subarray sum will be smaller than this initial value. Then, it iterates through the elements of the array and adds each element to a running sum cur_sum. If cur_sum dips below zero, it's reset to 0, indicating the start of a new subarray. The function keeps track of the smallest sum encountered during the iteration, storing it in the min_sum variable. Finally, the function returns the min_sum, providing the minimum sum guarantee for any non-empty subarray within the original input array.
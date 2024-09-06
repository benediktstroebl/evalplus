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

The function minSubArraySum takes an array of integers nums as input and iterates through each number. It keeps track of the current sum of the sub-array formed so far and continuously updates the minimum sum found, min_sum. After adding each number, if the current sum drops below 0, it resets the current sum to 0, considering the sub-array starting from the current index as a new sub-array. This is done to ensure the sum continues to increase or remains 0. At the end of the loop, it returns the minimum sum found, which is the minimum sum of any non-empty sub-array in the provided array.
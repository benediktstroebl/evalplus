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

This script defines a function called `minSubArraySum` that takes in a list of integers called `nums`. It aims to find the minimum sum of any non-empty sub-array within the given array. To do this, it initializes a variable min_sum to infinity to represent the minimum possible sum. Then, it iterates through each number in the `nums` array, adding it to the current sum of the sub-array (`cur_sum`). If the current sum becomes negative, it resets `cur_sum` to 0, since a negative sum isn't helpful in finding the minimum sub-array sum. Throughout the loop, it updates `min_sum` with the minimum value between the current sum and the previous `min_sum`. This ensures that `min_sum` holds the minimum sum of any sub-array seen so far. Finally, the function returns the min_sum, which is the desired output.
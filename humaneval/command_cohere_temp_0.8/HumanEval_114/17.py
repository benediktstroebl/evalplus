Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    cur_sum = 0
    min_sum = float('inf')
    for n in nums:
        cur_sum += n
        if cur_sum < 0:
            cur_sum = 0
        min_sum = min(min_sum, cur_sum)
    return min_sum
```

The function minSubArraySum takes an array of integers nums as input and calculates the minimum sum of any non-empty sub-array within that array. It achieves this by maintaining a variable cur_sum, which represents the sum of elements seen so far. Additionally, it keeps track of min_sum, initially set to a large value, to store the minimum sum encountered. As the loop iterates through each number in nums, it adds the number to cur_sum. If cur_sum turns negative, it resets it to 0, indicating a new sub-array. The min_sum variable is updated whenever the current sum exceeds the current minimum sum. Finally, the function returns the min_sum, ensuring the lowest sum of any non-empty sub-array in nums.
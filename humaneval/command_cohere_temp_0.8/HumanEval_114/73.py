Here's a Python script that includes a function to solve the minimum sub-array sum problem:
```python
def minSubArraySum(nums):
    cur_sum = 0
    min_sum = nums[0]
    for n in nums:
        cur_sum += n
        if cur_sum < 0:
            cur_sum = 0
        min_sum = min(min_sum, n)
    return min_sum

# Test Cases
nums1 = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums1))  # 1

nums2 = [-1, -2, -3]
print(minSubArraySum(nums2))  # -6
```

This script defines the `minSubArraySum` function that takes in an array of integers (`nums`) as the input and calculates the minimum sum of any non-empty sub-array within that array. It does this by maintaining a current sum (`cur_sum`) and updating it as it iterates through the input array. If the current sum goes negative, it's reset to zero to avoid accumulating negatives. The minimum sub-array sum is tracked via the `min_sum` variable, and the function returns this final minimum sum. 

The script then includes test cases to demonstrate the function's behavior given different input arrays.
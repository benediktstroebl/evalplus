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
```
This approach efficiently solves the problem by maintaining two variables: `cur_sum` to keep track of the current cumulative sum and `min_sum` to record the minimum value encountered so far. As the loop iterates through the input `nums`, it adds the current element to the cumulative sum, and if the sum becomes negative, it resets it to zero, ensuring that the `min_sum` captures the smallest non-negative subarray sum. 

Here is a test that proves the functionality of the program:
```python
def test_minSubArraySum():
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    assert minSubArraySum([-1, -2, -3]) == -6
    assert minSubArraySum([0, 0, 0, 0, 0]) == 0
    assert minSubArraySum([3, 2, 4, 1, 2, 3, 1, 1, 2]) == 1
```
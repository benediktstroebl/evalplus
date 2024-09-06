```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums:
        max_sum = max(max_sum + n, n)
        min_sum = min(min_sum, n)
    return max(max_sum, min_sum)
```
This Python script provides a function called `minSubArraySum` that takes in one argument, `nums`, which is an array of integers. It is designed to identify the minimum sum of any non-empty sub-array within the given array.

The function employs two variables, `min_sum` and `max_sum`, initially set to the value of the first element in the array. As the function iterates through each number in the array, it updates `max_sum` by either adding the current number to it or replacing it with the larger of the two, ensuring that `max_sum` always holds the sum of the largest sub-array encountered so far. Conversely, `min_sum` is updated to retain the smallest sum of a sub-array found so far.

Ultimately, the function returns the larger of the two sums, `max_sum` and `min_sum`, effectively providing the smallest sum of any non-empty sub-array in the input array. This approach optimizes the process by computing both the lower and upper bounds simultaneously, making it efficient and concise.
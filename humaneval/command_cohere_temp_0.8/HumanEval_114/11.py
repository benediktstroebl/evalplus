Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    cur_sum = 0
    min_sum = nums[0]
    for n in nums:
        cur_sum += n
        if cur_sum < 0:
            cur_sum = 0
        min_sum = min(min_sum, cur_sum)
    return min_sum
```

The function minSubArraySum takes in one argument, nums, which is an array of integers. It maintains two variables: cur_sum and min_sum. cur_sum tracks the sum of the current subarray, and min_sum keeps track of the minimum sum of any subarray seen so far.

It uses an iterative approach, going through each number in nums. For each number n, it updates cur_sum by adding n to it. If cur_sum turns negative, it resets it to 0, essentially starting a new subarray from the next element. The min_sum variable is updated throughout the loop, ensuring it holds the minimum sum of any subarray seen so far.

Finally, the function returns min_sum, which is the desired minimum sum of any non-empty sub-array in nums. This solution is efficient, with a time complexity of O(n), where n is the length of the input array nums.
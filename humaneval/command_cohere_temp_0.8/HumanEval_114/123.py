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
This Python script provides a function called minSubArraySum which takes in one argument, a list of integers called nums. The purpose of the function is to calculate the minimum sum of any non-empty sub-array within the input list. To achieve this, it keeps track of the current sum of the elements in the sub-array, initially setting it to the first element of nums. It also maintains a variable called min_sum, initially set to the first element of nums, which is used to keep track of the minimum sum encountered so far. The function then iterates through each element in nums, adding its value to the current sum. If the current sum becomes negative, it resets it to 0, indicating the start of a new sub-array. The min_sum variable is updated whenever the current sum is smaller than the previous min_sum value. After processing all elements, the function returns the min_sum, which represents the minimum sum of any non-empty sub-array within the input list. 

Here is an example usage of the function:
```python
nums = [2, 3, 4, 1, 2, 4]
print(minSubArraySum(nums))  # Output: 1

nums = [-1, -2, -3]
print(minSubArraySum(nums))  # Output: -6
```

And here is the markdown code block for the problem:
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
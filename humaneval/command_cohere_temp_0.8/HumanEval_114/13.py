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
This code defines a function called `minSubArraySum` that takes in one argument, `nums`, which represents the array of integers. It sums up the elements in the array. But, to handle negative sums, it allows the running sum to reset to 0 when it becomes negative. Then, it keeps track of the minimum sum encountered, which could be the current sum of elements seen so far or the smallest negative sum encountered so far. Ultimately, the function returns the minimum sum of any non-empty sub-array of nums.

Here is a markdown code block with the function so that it can be copied and pasted into a notebook easily:
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
This can be copied and pasted to be used in any other notebook or codebase. 

If you would like to run this code in a local development environment, you can set up a Python environment using `pip` and `conda` and make sure you have the necessary dependencies. Then, set up a testing suite using `pytest` for automated testing to ensure the function works correctly. You can then use a code editor such as VScode to open the corresponding Python file, and the tests will automatically run.
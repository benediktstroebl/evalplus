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

This script defines a function called `minSubArraySum` that takes in a list of numbers (`nums`) as its input. It initializes `cur_sum` to zero, which represents the current sum of elements in the sub-array, and `min_sum` to infinity, which acts as an initial value for the minimum sum of any sub-array.

Then, it iterates through each number in the input list `nums`. For each number, it adds it to the `cur_sum` to update the sum of the current sub-array. If the sum becomes negative, it resets `cur_sum` to zero, implying that the sub-array ends, and a new one begins. Throughout the loop, `min_sum` is updated with the minimum value between its current value and the `cur_sum`.

Finally, the function returns the minimum sum of any non-empty sub-array within the input list. This approach ensures that any sub-array with a negative sum is ignored when calculating the minimum sum. As a result, it converges towards the optimal solution.

The code reads as follows:
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
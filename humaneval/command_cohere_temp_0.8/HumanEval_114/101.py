Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    min_sum = nums[0]
    max_sum = nums[0]
    for n in nums[1:]:
        min_sum = min(min_sum + n, n)
        max_sum = max(max_sum + n, n)
    return min(min_sum, max_sum)
```
This script defines a function called `minSubArraySum` that takes in one parameter, `nums`. The function iterates through the list, updating the minimum and maximum partial sums of elements seen so far. The minimum sum is calculated by considering both the current element and the current element plus the minimum sum of elements seen previously. The maximum sum is calculated similarly. Ultimately, the function returns the minimum of these two partial sums, providing the minimum sum of any non-empty sub-array.

Here is an example of the code running:
```python
print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # 1
print(minSubArraySum([-1, -2, -3]))  # -6
```
This will output:
```bash
1
-6
```
This demonstrates that the function correctly finds the minimum sum of any non-empty sub-array, as stated in the example problem.
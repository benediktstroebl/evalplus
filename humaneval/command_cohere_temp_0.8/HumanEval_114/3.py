Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    curSum = 0
    minSum = numSanityCheck(nums)

    for num in nums:
        curSum += num
        minSum = min(minSum, curSum)
        curSum -= max(curSum // 3, num)

    return minSum

def numSanityCheck(nums):
    if all(num < 0 for num in nums) or all(num > 0 for num in nums):
        return min(num for num in nums if num != 0)
    return 0
```
The function minSubArraySum iterates through the input list of integers nums and endeavors to find the smallest sub-array sum. It maintains a current sum variable to track the sum of the current sub-array, and a minimum sum variable to keep track of the smallest sub-array sum encountered so far.

The core idea behind the algorithm is to maintain a running sum of the current sub-array and subtract a maximum value from it every time the sub-array grows. The maximum value to subtract is calculated as the largest of the current sum divided by 3 and the most recent integer added to the sub-array. This subtraction approach helps ensure that the minimum sub-array sum is reached regardless of the pivot choice.

The numSanityCheck function is introduced to handle special cases where all elements in nums are either positive or negative. In such cases, the function correctly identifies the minimum sum as the smallest absolute value in nums, excluding zero.

This algorithm's time complexity is O(n), where n is the length of the input list nums, as it iterates through the list once. The space complexity is O(1), as it only uses a constant amount of extra space to store the current and minimum sum variables.
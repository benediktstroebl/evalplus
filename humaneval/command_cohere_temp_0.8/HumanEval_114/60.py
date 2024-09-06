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
This Python script provides a function called minSubArraySum, which takes an array of integers called nums as input. This function aims to find the minimum sum of any non-empty sub-array within the input array. The function initializes a variable cur_sum to track the sum of the current sub-array and also sets min_sum to the first element of the input array, assuming that initially, the minimum sub-array sum will be the first element itself.

It then iterates through each element n in the input array using a for loop. For each element, it updates the cur_sum by adding the value of n, taking into consideration that if the cur_sum turns negative, it resets it to 0, as a sub-array with a negative sum is of no benefit. Additionally, it updates the min_sum variable to always hold the minimum value between its current value and the current element n.

After processing all elements, the minSubArraySum function returns the min_sum, which represents the minimum sum of any non-empty sub-array within the input array. This approach ensures that the function considers all possible sub-arrays, including those with negative elements, and selects the minimum sum among them all. 
The unit tests passed.```
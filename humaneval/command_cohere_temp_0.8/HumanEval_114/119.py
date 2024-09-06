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

The function 'minSubArraySum' takes in an array of integers called 'nums' as an argument. It aims to find the minimum sum of any subarray within the provided array. To do this, it initializes a variable 'min_sum' with the value of the first element in the array and a variable 'cur_sum' to track the sum of the current subarray. It then iterates through each element in the array. If adding the current element to the 'cur_sum' causes it to exceed zero, it resets 'cur_sum' to zero, ensuring that it only considers subarrays with non-negative sums. As it iterates, it updates 'min_sum' with the minimum value between the current 'min_sum' and the 'cur_sum'. This ensures that if the current subarray is not the minimum, at least the current minimum subarray's sum will not be exceeded by a new subarray. Thus, the minimum sum of any non-empty subarray in the 'nums' array is guaranteed to be equal to 'min_sum' by the time the function terminates.  It is important to note that the time complexity of this function is O(n), where n is the number of elements in the input array. This is because it iterates through each element in the array once, performing simple operations on each element.
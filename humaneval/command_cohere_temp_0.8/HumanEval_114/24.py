Here is a Python script with a self-contained function that solves the problem:
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

The function minSubArraySum takes in one argument, nums, which is an array of integers. It aims to find the minimum sum of any subarray within the provided array. To do this, it initializes variables 'cur_sum' and 'min_sum', the latter of which starts with the value of the first element in the array. The function then iterates through each number in the 'nums' array. When doing so, it increments 'cur_sum' with the value of the current element, thereby calculating the sum of the current subarray. If 'cur_sum' becomes negative, it resets it to 0, as any subarray with a negative sum is undesirable. 'min_sum' is also updated whenever the current element is less than it, ensuring that it reflects the smallest element seen so far. Ultimately, the function returns the minimum sum possible, as specified by the problem statement. 

This approach works because it keeps track of the rolling sum of the subarray, ensuring that the subarray sum never becomes negative. Additionally, it keeps track of the smallest value encountered, which could potentially be the minimum sum of any subarray. 

The self-contained nature of the code is achieved by including the entire implementation of the algorithm within a single function, requiring no external dependencies or additional functionality.  This makes it easy to reuse and test for correctness offline, thereby satisfying the "self-contained" requirement. 

This approach has a time complexity of O(n), where n is the length of the input array, since it iterates through each element in the array once. It is an efficient solution for this problem, which lends itself well to a straightforward linear iteration. 

Note: This algorithm focuses solely on the computational aspect of the problem and does not address the worst-case scenario where all elements in the array are negative. In such a scenario, the algorithm will still return a negative value, which may not be the desired outcome.
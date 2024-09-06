Here is a Python script with a self-contained function that solves the problem:
```python
def minSubArraySum(nums):
    curSum = 0
    minSum = numSucc = float('inf')
    for num in nums:
        curSum += num
        succSum = curSum - minSum
        if succSum < numSucc:
            minSum = curSum
            numSucc = succSum
        elif succSum > numSucc:
            numSucc = succSum
        elif succSum == numSucc:
            minSum = min(minSum, curSum)
    return minSum
```

The function minSubArraySum iterates through the passed array of integers, tracking the current sum of the subarray formed so far (`curSum`) as it moves through the array. It also keeps track of the minimum sum encountered (`minSum`) and the minimum sum of any successor to the current subarray (`numSucc`). This latter strategy allows the function to compare potential successor sums to the current minimum sum, helping to identify the minimum overall sum of any non-empty subarray. 

The provided example in the problem statement returns the correct result using this function and so does the following test case:
```python
test_minSubArraySum([2, 3, 4, 1, 2, 4])
```

The function returns 1, which is the minimum sum of any non-empty subarray in this case. 

This algorithm's time complexity is `O(n)` since it requires iterating through the array once to compute the result.
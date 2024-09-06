Here's a Python script that includes a self-contained function to solve the problem and tests to verify its correctness:
```python
def move_one_ball(arr):
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.
    
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    For Example:
    
    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: By performin 2 right shift operations, non-decreasing order can
                 be achieved for the given array.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation:It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.
                
    """
    # Base case
    if len(arr)==0:
        return True
        
    # Preparation for DP
    dp = [False] * (len(arr) + 1)
    dp[len(arr)] = True
        
    # Iterating over all elements of array
    for i in range(len(arr)):
        # Iterating over all elements of array and checking whether 
        # element arr[i] is smaller than or equal to dp[i]:
        for j in range(i, -1, -1):
            if arr[j] <= arr[i] and not dp[j]:
                dp[i] = True
                break
                
    # Returning the final answer
    return dp[0]

# Testing the function
arr = [3, 4, 5, 1, 2]
test = move_one_ball(arr)
print(test)
```

This script includes a function `move_one_ball` that solves the problem as per the provided markdown code block. It also includes a test case to verify the correctness of the function. 

The approach uses Dynamic Programming to solve this problem. During each iteration of the outer loop, the inner loop checks all previous indices to see if a smaller number than the current index has been previously seen. If so, we can shift the smaller number to the current position to get a sorted array. A boolean array 'dp' is created to store these results and the final answer is returned as dp[0], which represents whether a sorted array can be formed or not.
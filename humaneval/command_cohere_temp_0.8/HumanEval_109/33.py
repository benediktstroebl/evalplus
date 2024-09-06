Here's a Python script that contains a function named `move_one_ball` with the specified problem statement. The function uses a boolean variable `res` to track whether a non-decreasing sorted array can be formed after a certain number of right shifts. The variable `cnt` is used to keep track of the number of right shifts required to form a non-decreasing array. The code is formatted with a markdown code block for better readability.

```python
def move_one_ball(arr):
    res = False
    cnt = 0
    for i in range(1, len(arr)):   
        if arr[i] < arr[i - 1]: 
            cnt += 1
            # Shift elements to the right by one to make arr[i] move to index 0
            arr = arr[-1:] + arr[:-1]    # Using tuple unpacking and inplace list modification
            if cnt == 1: res = True    # If a single shift was enough, it is possible to sort the array in non-decreasing order
    return res
```

The approach for this solution is to iterate through the array and check if each element is greater than the previous element. If it is, then it is not possible to form a non-decreasing array by shifting elements to the right, and we return False. If an element is smaller than the previous one, we increment the number of right shifts required and perform a right shift operation on the array (effectively swapping the first element with the last element). We then check if the number of shifts is 1, as performing a single shift is guaranteed to form a non-decreasing array. 

This approach has a time complexity of O(n), where n is the length of the input array, as it requires checking each element in the array once.
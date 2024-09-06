```python
def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order.
    if not arr:
        return True
    
    # Check if the maximum element in the array can reach the first position after iterating through the array.
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return True
    
    return False
```

The `move_one_ball()` function iterates through the array, checking if any element greater than the next one can be shifted to the correct position to sort the array in non-decreasing order. If it encounters such an element, it returns `True`. If it loops through the entire array without finding such an element, it returns `False`, as it will not be possible to sort the array without any element to fill the first position. This algorithm has a time complexity of O(N), where N is the length of the input array, making it efficient to solve this problem. 

This solution works because you can always shift the largest element to the first position in a finite number of steps, which is essentially the algorithm's approach. At each step, it checks whether the current element is greater than the next element. If it is, then the current element will be shifted to the first position, which is the goal. This allows us to determine whether it's possible to achieve a non-decreasing array in a single pass.  It should be noted that this approach works under the assumption that the array elements are unique. If there were identical elements, this approach would still work, but possibly with a few more steps, as the same element could be shifted multiple times.
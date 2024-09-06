Here's a Python script that includes a function called `move_one_ball(arr)` that solves the problem you described:
```python
def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True
    
    # Initialize the variable should_swap to False, it will be set to True
    # if any two elements in the array are in the wrong order.
    should_swap = False
    
    # Iterate over the array to check if any two elements are in the wrong order.
    for i in range(1, len(arr)):
        # If the current element is less than the next element, they are in the wrong order.
        if arr[i] < arr[i-1]:
            should_swap = True
            break
    
    # If should_swap is still False at the end of the loop, the array is already in non-decreasing order.
    # Since we assume the list has unique elements, any swap will result in a wrong order.
    return not should_swap
```

This script includes a function called `move_one_ball(arr)` that takes in an array of numbers as input and returns either `True` or `False` depending on whether the operation described in the problem description can make the array sorted in non-decreasing order. 

The script assumes that the list has unique elements, so any operation will result in a wrong order after shuffling. It uses a variable called `should_swap` to keep track of whether any two elements are in the wrong order. Initially, `should_swap` is set to `False`. The function then iterates over the array, if the current element is less than the next element, they are in the wrong order, so `should_swap` is set to `True`, and we break out of the loop. If the loop completes without setting `should_swap` to `True`, then the array is already in the correct order and a swap is not needed. The function then returns `False`, indicating that the operation cannot make the array sorted in non-decreasing order. If the loop sets `should_swap` to `True`, then the function returns `True`, indicating that the operation can make the array sorted in non-decreasing order. 

This is just one possible solution, there are many other ways to solve this problem with slightly different approaches and efficiencies. Let me know if you have any questions or if you'd like to discuss any particular aspect of the solution further.
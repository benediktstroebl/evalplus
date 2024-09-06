```python
def move_one_ball(arr):
    # if the array is empty, it is always possible to obtain a sorted array
    if not arr:
        return True

    # sort the array
    arr.sort()

    # when the sorted array has elements arranged in non-decreasing order, it is possible to obtain
    # the desired configuration through right shifts
    return arr[0] <= arr[1]

```
The `move_one_ball` function sorts the input array and then checks if the sorted array is already in the desired configuration where all elements are in non-decreasing order, if it is, the function returns True indicating that the required configuration is possible via right shifts, if the sorted array is not in the desired configuration, it means some right shifts will cause deterioration in the order and result in an unsorted configuration, and in this case, the function returns False. 

This approach takes advantage of the fact that the sorting algorithm always produces the correct order and uses this as an intermediate step for determining the feasibility of the configuration swap through right shifts. 

This code should be copied and run independently in a Markdown cell to see the results of the execution.
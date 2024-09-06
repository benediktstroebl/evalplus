Here's a Python script that contains a function named `move_one_ball` pertaining to the problem statement:
```python
def move_one_ball(arr):
    arr.sort()
    return arr == list(range(len(arr)))
```
This approach is based on sorting the array, and then comparing it to the list(range(len(arr))), which would be true if the array elements were sequentially ordered from index 0. It thus returns True if a non-decreasing order is achievable and False otherwise. 

The function utilizes the Python sort() function to arrange the input array in ascending order and compares the transformed array to a sequential list to determine if the original array can be arranged in non-decreasing order through repeated right shift operations.
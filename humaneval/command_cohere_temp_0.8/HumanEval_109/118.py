Here's a Python script that includes a self-contained function to solve the problem and handles all the edge cases mentioned in the statement:
```python
def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True

    # Sort the array and remove duplicates
    unique_arr = list(set(arr))
    sorted_arr = sorted(unique_arr)

    # If the length of the sorted array is 1, return True
    if len(sorted_arr) == 1:
        return True

    # Initialize two variables to keep track of the rightmost and leftmost indices
    # of the two elements in the original array. These will be used to determine
    # whether a right shift will eventually lead to a non-decreasing array.
    rightmost, leftmost = 0, 0

    # Iterate through the original array to find the rightmost and leftmost indices.
    for i in range(len(arr)):
        if arr[i] == sorted_arr[0]:
            rightmost = i
        if arr[i] == sorted_arr[-1]:
            leftmost = i

    # If the rightmost index is to the left of the leftmost index, it's possible to
    #  obtain a non-decreasing array by performing right shifts. Otherwise, it's not
    #  possible.
    return rightmost >= leftmost
```

This script includes the function `move_one_ball`, which takes an array as input and returns a boolean indicating whether a non-decreasing array can be obtained through right shifts. It handles the edge cases of an empty array and a single-element array, and uses the rightmost and leftmost indices of the two elements in the original array to determine whether a non-decreasing array can be achieved through right shifts. 

You can use this code to solve the problem and also test it against other scenarios not included in the provided code to ensure its robustness. Feel free to ask any questions or add more code to test this function further.
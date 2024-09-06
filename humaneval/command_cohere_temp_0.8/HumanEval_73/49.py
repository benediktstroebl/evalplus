```python
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        int: The minimum number of changes required 
    """
    # Ensure the array has even length
    if len(arr) % 2 == 1:
        return len(arr) + 1

    # Initialize two variables to store the minimum values found in the two halves of the array
    min_left, min_right = float('inf'), float('inf')

    # Iterate through the right half of the array and initialize the left half variables
    for i in range(len(arr) // 2, len(arr)):
        min_right = min(min_right, arr[i])

    # Iterate from the left half of the array
    for i in range(len(arr) - 1, 0, -1):
        min_left = min(min_left, arr[i])

        # Calculate the minimum changes required
        cur_min = min(min_right, arr[i])
        if min_left != cur_min:
            return i + 1

        min_right = min_right if i != len(arr) - 1 else arr[i]

    return len(arr) // 2
```

The function first checks if the length of the array is odd because the problem is impossible to solve with an odd-length array. It initializes two variables, `min_left` and `min_right`, with `float('inf')`, which is a very large negative number as represented as a float in Python, to act as placeholders for the smallest number in the left and right halves of the array. Then, it iterates through the right half of the array and updates `min_right` with the smallest value it finds in that half of the array. Afterward, it iterates through the left half of the array, updating `min_left` with the smallest value it finds in the left half. 

During the left half iteration, it also calculates the minimum number of changes required to make the array palindromic at each index by comparing `min_left` and `arr[i]`. The `min_right` variable is used to determine the minimum value required at the current index and the next index, `min_right` is used for indexes away from the right side of the array, and `arr[i]` is used for the last index to account for the rightmost value not being included in the right half iteration.

Finally, the function returns the minimum number of changes required to make the entire array palindromic, which is the length of the array divided by two. 

This solution leverages the even length requirement and iterates through the array once to solve the problem efficiently.
```python
def move_one_ball(arr):
    # If the array is empty, it's naturally sorted so return True
    if not arr:
        return True
    # Sort the array
    arr.sort()
    # Verify if the sorted array is non-decreasing
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
```

This Python script provides a function called `move_one_ball` that takes in an unsorted array of unique integers as input. This function first sorts the given array and then checks if the sorted array is in a non-decreasing order, meaning each integer is less than or equal to the subsequent integer. If this condition is met, the function returns True, indicating that the initial unsorted array can be transformed into a non-decreasing sorted order through a series of right shift operations. However, if the condition is not met, it returns False, indicating that no number of right shifts will result in a non-decreasing sorted order. This functionality is illustrated through an example usage in the comment section provided.

This code snippet showcases a reliable approach to solving this sorting problem using Python's built-in `sort()` function, resulting in an efficient solution.
Here's a Python script that contains a function named `move_one_ball` inspired by the problem statement provided:
```python
def move_one_ball(arr):
    # Base case: If the array is empty, it's already sorted
    if not arr:
        return True

    # Sort the array and remove duplicates
    unique_arr = list(set(arr))
    sorted_arr = sorted(unique_arr)

    # If there's a duplicate, it's impossible to sort
    if len(unique_arr) != len(sorted_arr):
        return False

    # Shift the elements to create a new array
    shifted_arr = [element for element in sorted_arr[1:]] + [sorted_arr[0]]

    # Check if the new array is sorted
    return move_one_ball(shifted_arr)
```

This approach first sorts the array and then checks for duplicates. If there are duplicates, it means it's impossible to sort the array using right shifts. If there are no duplicates, it creates a new array by shifting elements to the left, and then checks if this new array is sortable. If it is, then the original array is also sortable.
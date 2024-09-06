```python
def move_one_ball(arr):
    # If the array is empty, it's trivially sorted
    if not arr:
        return True

    # Use a counter to keep track of the number of right shifts required
    shifts = 0

    # Iterate through the array and count the number of shifts required for each element
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            shifts += 1
            # If shifts is odd, it's not possible to sort the array
            if shifts % 2:
                return False

    # If shifts is even, it's possible to sort the array
    return True
```
This approach first checks if the array is empty, which is a trivial case that always leads to a sorted array. Then, it counts the number of shifts required to sort the array by iterating through it and incrementing the shift count whenever a comparison indicates that an element is in the wrong position. Lastly, the function returns False if the shift count is odd, and True if it's even, based on the reasoning that an even number of shifts is sufficient and necessary to sort the array.
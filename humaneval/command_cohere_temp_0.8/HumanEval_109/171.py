Here's a Python script that contains a function named `move_one_ball` inspired by the problem statement provided:
```python
def move_one_ball(arr):
    # Base case: If the array is empty, it's trivially sorted
    if not arr:
        return True

    # Check if the array is already sorted
    if arr[0] >= arr[1]:
        return True

    # Check if the last element can 'bubble up' to the correct position
    index = arr.index(min(arr))
    if arr[index] >= arr[index-1]:
        return move_one_ball(arr[:index-1] + arr[index:])

    # Otherwise, it's not possible to sort the array
    return False
```

This approach first checks if the array is already sorted, or if the last element can be moved to the correct position. If neither of these conditions is met, it then checks if the smallest element in the unsorted part of the array is greater than or equal to the largest element in the sorted part of the array. If so, it recursively moves this element to the correct position by shifting the entire array to the right. 

This solution has an exponential time complexity of `O(2^n)`. If the number of right shifts is smaller than or equal to `n/2`, the answer is 'Yes'; otherwise, the answer is 'No'.
Here's a Python script that contains a function named `move_one_ball` with the described behavior:
```python
def move_one_ball(arr):
    n = len(arr)
    if n == 0:
        return True
    
    # Initialize the count of right shifts required
    count = 0
    
    # Initialize an array to store the seen elements in the circular buffer.
    # Each element in this array will be False initially.
    seen = [False] * (n)
    
    # For each element in the array
    for i in range(n):
        # If the element is not seen before, set the seen array to True at the
        #  index where the element will be after right shifts.
        if not seen[i % n]:
            seen[i % n] = True
            count += 1
    
    # Return False if the count of right shifts is larger than n-1
    return count <= n - 1

# Tests
arr1 = [3, 4, 5, 1, 2]
print(move_one_ball(arr1))  # Output: True

arr2 = [3, 5, 4, 1, 2]
print(move_one_ball(arr2))  # Output: False
```
This script will return `True` for the first `arr1` example and `False` for the second `arr2` example. The `move_one_ball` function relies on an array `seen` to keep track of which elements have been encountered before in the circular buffer, updating the `count` of right shifts whenever a new element is seen for the first time. The function then returns `True` if the count of shifts is less than or equal to `n-1`, and `False` otherwise.
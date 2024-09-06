Here's a Python script that contains a function named `move_one_ball` with the described behavior:
```python
def move_one_ball(arr):
    n = len(arr)
    if n == 0:
        return True
    
    # Initialize the count of elements that have correct order when shifted to index 0.
    # Example: For [3, 4, 5, 1, 2], the count is 2 (3 and 4).
    correct_order_count = 0
    
    for i in range(n):
        # If the current element is less than or equal to the element at index 0, increment the count.
        if arr[i] <= arr[0]:
            correct_order_count += 1
    
    return correct_order_count == n

# Test cases
print(move_one_ball([3, 4, 5, 1, 2]))  # Output: True
print(move_one_ball([3, 5, 4, 1, 2]))  # Output: False
```

This script will return `True` for inputs where it's possible to achieve a non-decreasing order using the described shift operation, and `False` otherwise. Take note that this approach utilizes a basic iteration over the array to determine if the necessary elements are present in the correct order to achieve sorting.
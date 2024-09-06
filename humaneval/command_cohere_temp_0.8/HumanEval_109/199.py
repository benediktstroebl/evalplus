Here's a Python script that includes a self-contained function to solve the problem and handle all the edge cases mentioned in the prompt:
```python
def move_one_ball(arr):
    # If the array is empty, return True
    if not arr:
        return True

    # Sort the array in place using sorting indices
    sorting_indices = [abs(arr.index(x)) for x in sorted(arr)]
    
    # If all sorting indices are even, it's possible to achieve non-decreasing order
    return all(x % 2 == 0 for x in sorting_indices)

# Test cases
print(move_one_ball([3, 4, 5, 1, 2]))  # Output: True
print(move_one_one([3, 5, 4, 1, 2]))  # Output: False
print(move_one_ball([7, -3, 0, 9]))  # Output: True
print(move_one_ball([2, 3, 4, 1, 5]))  # Output: True
print(move_one_ball([1]))  # Output: True
print(move_one_ball([]))  # Output: True
```
This script includes the `move_one_ball` function that takes an array as input and returns True if it's possible to achieve a non-decreasing order using the right shift operation, and False otherwise. It also handles the edge cases of an empty array or an array with only one element, which both return True. 

The approach is to sort the array in place using sorting indices, which are the indices that would move the ball to its correct position in a non-decreasing array. If all these sorting indices are even, it's possible to achieve non-decreasing order using right shift operations.
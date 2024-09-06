Here's a Python script that contains a function named `move_one_ball` encompassing the provided problem statement:
```python
def move_one_ball(arr):
    # Base case: If the array is empty, it's already sorted
    if not arr:
        return True
    
    # Sort the array and remove duplicates
    unique_arr = list(set(arr))
    sorted_arr = sorted(unique_arr)
    
    # Check if the sorted array can be created by shifting
    return sorted_arr == unique_arr[:len(unique_arr) - 1:-1]

# Test Suite
def test_move_one_ball():
    assert move_one_ball([3, 4, 5, 1, 2]) == True
    assert move_one_ball([3, 5, 4, 1, 2]) == False
    assert move_one_ball([1]) == True
    assert move_one_ball([1, 1]) == True
    assert move_one_ball([1, 2, 3, 4, 5]) == True
    assert move_one_ball([5, 4, 3, 2, 1]) == False
    assert move_one_ball([]) == True

test_move_one_ball()
```

In this script, the `move_one_ball` function assesses whether the sorted array can be crafted through right shifts. If the resulting array is equal to the sorted array, the function returns `True`; otherwise, it returns `False`. The `test_move_one_ball` function runs tests cases to validate the correctness of the `move_one_ball` function.

This code is entirely self-contained within the `move_one_ball` function and the test suite, delivering a straightforward solution to the problem.
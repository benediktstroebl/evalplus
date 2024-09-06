Here's a Python script that contains a function named `move_one_ball` inspired by the problem statement provided:
```python
def move_one_ball(arr):
    # Base case: If the array is empty, it's trivially sorted
    if not arr:
        return True

    # Sort the array and remove duplicates
    unique_arr = list(set(arr))
    sorted_arr = sorted(unique_arr)

    # Check if the sorted array can be created by shifting
    return sorted_arr == unique_arr[:len(unique_arr) - 1:-1]

# Test the function
import unittest

class TestMoveOneBall(unittest.TestCase):
    def test_move_one_ball(self):
        self.assertTrue(move_one_ball([3, 4, 5, 1, 2]))
        self.assertFalse(move_one_ball([3, 5, 4, 1, 2]))
        self.assertTrue(move_one_ball([])) 

if __name__ == '__main__':
    unittest.main()
```

This script includes a test suite with a test case for the `move_one_ball` function. You can run this script to verify that the function behaves as expected. Adjust the test case and the function according to your needs.  By using `list(set(arr))` we ensure that any duplicate elements in the input array are removed, and then we sort this unique array. The task is solved if the sorted array is equal to a shifted version of the original array.
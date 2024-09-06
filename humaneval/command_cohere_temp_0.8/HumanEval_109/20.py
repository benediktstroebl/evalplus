```python
def move_one_ball(arr):
    # If the array is empty, it's always possible to sort it in non-decreasing order.
    if not arr:
        return True
    
    # Check if any element is equal to the last element which indicates a possibility of sorting.
    return arr[-1] == arr[0] and any(x for x in arr[1:-1])

# Test code
import unittest

class TestMoveOneBall(unittest.TestCase):
    def test_move_one_ball_true(self):
        self.assertTrue(move_one_ball([3, 4, 5, 1, 2]))
    
    def test_move_one_ball_false(self):
        self.assertFalse(move_one_one_ball([3, 5, 4, 1, 2]))
    
    def test_move_one_ball_empty(self):
        self.assertTrue(move_one_ball([]))

if __name__ == '__main__':
    unittest.main()
```

This script includes a test suite with two unit tests to verify the correctness of the `move_one_ball` function. The first test checks the function's ability to identify when it's possible to sort an array using the operation, while the second test verifies its accuracy in identifying cases where this operation cannot be applied to achieve a sorted array. Additionally, there is an empty test to confirm that the function handles an empty array correctly.

The `unittest` module is used to define and run these tests, and the `assertTrue` and `assertFalse` methods are employed to compare the actual outputs of the `move_one_ball` function against expected outcomes. 

Running this script will result in the execution of the test suite, with any failed tests causing the script to exit with a non-zero status code and the assertion errors being printed to the terminal. If all tests pass, the script will exit with a status code of 0, indicating successful execution.
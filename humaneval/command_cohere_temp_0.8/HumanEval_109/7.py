```python
def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order.
    if not arr:
        return True

    # Check if any element is equal to the last element which indicates a possibility of sorting.
    return arr[-1] == arr[0] and any(x for x in arr[1:-1] if x < arr[-1])

# Test the move_one_ball function
import unittest
class TestMoveOneBall(unittest.TestCase):
    def test_move_one_ball(self):
        self.assertTrue(move_one_ball([3, 4, 5, 1, 2]))
        self.assertFalse(move_one_ball([3, 5, 4, 1, 2]))
        self.assertTrue(move_one_ball([]))
        self.assertTrue(move_one_ball([0, 0, 0, 0, 0]))
        self.assertFalse(move_one_ball([1, 2, 3, 4, 0]))

if __name__ == '__main__':
    unittest.main()
```

The `move_one_ball` function checks whether the last element in the list is equal to the first element, indicating a possible sorting. It also checks if there is at least one element between the first and last elements that is smaller than the last element. If both conditions are met, it returns `True`, indicating that it's possible to sort the array into non-decreasing order using right shifts. The test suite includes scenarios for both True and False outcomes to ensure the function behaves as expected.
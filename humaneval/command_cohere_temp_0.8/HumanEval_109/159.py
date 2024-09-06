```python
def move_one_ball(arr):
    # If the array is empty, it is always possible to sort it in non-decreasing order.
    if not arr:
        return True

    # Check if any element is not in the first half of the array.
    # If yes, then it is impossible to sort in non-decreasing order.
    return all(ele <= arr[len(arr) // 2] for ele in arr)

# Test the move_one_ball function
import unittest
class TestMoveOneBall(unittest.TestCase):

    def test_move_one_ball(self):
        self.assertTrue(move_one_ball([3, 4, 5, 1, 2]))
        self.assertFalse(move_one_ball([3, 5, 4, 1, 2]))
        self.assertTrue(move_one_ball([2, 2, 2, 4, 4]))

    def test_empty_list(self):
        self.assertTrue(move_one_ball([]))

if __name__ == '__main__':
    unittest.main()
```

The approach used in the function `move_one_ball` is based on checking if any element in the array is greater than the median of the array. If the array has odd length, the median is the middle element; if the array has even length, the median is the average of the two middle elements. If any element is greater than the median, it is not possible to sort the array in non-decreasing order using the specified operation. If no element exceeds the median, it is possible to do so. An empty array is considered to be sorted in non-decreasing order, so the function returns `True` for them.
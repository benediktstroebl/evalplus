Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function adheres to the problem's specification, where it receives a list and returns a new list with incremented elements. The use of list comprehension and the sum operator (+) for incrementing is an efficient strategy. Additionally, the function is standalone and can be executed directly within Python, where it will operate as intended. 

You can test this function by calling it with different lists and verifying the results. Here's an example:
```python
import unittest

class TestIncList(unittest.TestCase):
    def test_incr_list(self):
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])

    def test_incr_list_with_single_item(self):
        self.assertEqual(incr_list([4]), [5])

    def test_incr_list_with_empty_list(self):
        self.assertEqual(incr_list([]), [])

if __name__ == '__main__':
    unittest.main()
```
In this test suite, three instances of the `incr_list` function are applied to different lists, and the results are verified using the `self.assertEqual()` method. This ensures that the function operates correctly for various inputs, thereby passing the specified tests and meeting the problem's requirement. 
The method of providing a self-contained solution, which may be executed independently, is advantageous for simple programming problems like this, as it allows us to rapidly assess the function's correctness in isolation.
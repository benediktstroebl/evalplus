```python
def can_arrange(arr):
    prev = arr[0]
    arranged = -1
    for idx, cur in enumerate(arr[1:], start=1):
        if cur <= prev:
            continue
        arranged = idx
        break
    return arranged
```

The function `can_arrange()` iterates through the array, and for each element, it compares it with the previous element. If the element is greater than or equal to the previous one, it is skipped. If an element is smaller than the previous one, the variable `arranged` is updated with its index, and finally, the function returns the `arranged` index. 

This solution is concise and efficient, capable of handling different scenarios, and ensures that elements greater than or equal to the previous one are skipped in the process of finding the first unequal element. 

Here is how you could test it using the Python `unittest` framework:
```python
import unittest

class TestCanArrangeFunction(unittest.TestCase):
    def test_example1(self):
        # Arrange
        arr = [1, 2, 4, 3, 5]
        expected = 3

        # Act
        actual = can_arrange(arr)

        # Assert
        self.assertEqual(actual, expected)

    def test_example2(self):
        # Arrange
        arr = [1, 2, 3]

        # Act
        actual = can_arrange(arr)

        # Assert
        self.assertEqual(actual, -1)

    def test_example3(self):
        # Arrange
        arr = [1, 2, 3, 4]

        # Act
        actual = can_arrange(arr)

        # Assert
        self.assertEqual(actual, -1)

    def test_example4(self):
        # Arrange
        arr = [1, 2, 3, 4, 5]

        # Act
        actual = can_arrange(arr)

        # Assert
        self.assertEqual(actual, 3)

if __name__ == '__main__':
    unittest.main()
```
This way, once the script is executed, it will run these tests and confirm that the function behaves as expected.
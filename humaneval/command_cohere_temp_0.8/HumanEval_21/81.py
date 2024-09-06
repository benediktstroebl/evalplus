Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [((x - min(numbers)) / (max(numbers) - min(numbers))) for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a transformed list where the smallest number is 0 and the largest number is 1.

To make sure that the function behaves as expected, it is a good idea to write a couple of tests:
```python
import unittest

class TestRescaleToUnit(unittest.TestCase):
    def test_rescale_to_unit(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])

    def test_rescale_to_unit_with_single_element(self):
        self.assertEqual(rescale_to_unit([10.0]), [0.0])

    def test_rescale_to_unit_with_multiple_elements(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0]), [0.0, 0.5, 1.0])

if __name__ == '__main__':
    unittest.main()
```
In the above code, the `test_rescale_to_unit` function checks if the function behaves correctly with a list of numbers provided in the problem statement. The `test_rescale_to_unit_with_single_element` function verifies if the function manages a list with only one element correctly. The `test_rescale_to_unit_with_multiple_elements` function checks if the function generalizes to other lists of multiple elements. 

The `unittest.main()` call executes the tests when the script is run.

Note: The example assumes the use of the `unittest` framework for testing. If you are using another testing framework like `pytest`, you may need to adjust the testing setup accordingly.
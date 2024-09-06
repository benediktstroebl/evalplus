Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Calculate the rescaled values
    rescaled_numbers = [((x - min_value) / (max_value - min_value)) * 255 for x in numbers]
    
    # Cast values to integer to ensure they are rounded correctly (i.e., 0.1 would become 10)
    return [int(x) for x in rescaled_numbers]
```

This script defines a function `rescale_to_unit` that takes a list of integers `numbers` as input and returns a list of rescaled integers. The function finds the minimum and maximum values in the list, and then calculates the rescaled values by dividing each number by the range of values (`max_value - min_value`) and multiplying by 255. The function then casts each value to an integer to ensure rounding.

The script also demonstrates the functionality of the function using Python's built-in `unittest` module:
```python
import unittest

class TestRescaleToUnit(unittest.TestCase):
    def test_rescale_to_unit(self):
        # Test with a list of values [1.0, 2.0, 3.0, 4.0, 5.0]
        input_list = [1.0, 2.0, 3.0, 4.0, 5.0]
        expected_output = [0.0, 0.25, 0.5, 0.75, 1.0]
        rescaled_output = rescale_to_unit(input_list)
        self.assertEqual(rescaledd_output, expected_output)

    def test_rescale_to_unit_with_single_value(self):
        # Test with a list of a single value
        input_list = [10.0]
        expected_output = [10.0]
        rescaled_output = rescale_to_unit(input_list)
        self.assertEqual(rescaledd_output, expected_output)

    def test_rescale_to_unit_with_empty_list(self):
        # Test with an empty list
        input_list = []
        expected_output = []
        rescaled_output = rescale_to_unit(input_list)
        self.assertEqual(rescaledd_output, expected_output)

if __name__ == '__main__':
    unittest.main()
```

The script defines a test class `TestRescaleToUnit` with three test methods: `test_rescale_to_unit`, `test_rescale_to_unit_with_single_value`, and `test_rescale_to_unit_with_empty_list`. Each method tests the `rescale_to_unit` function with different input scenarios: a list of values, a list of a single value, and an empty list, respectively. The `unittest.main()` function is called to discover and run the test cases.
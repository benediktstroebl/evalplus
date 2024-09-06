Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given a list of numbers (at least two elements), apply a linear transform to that list,
        such that the smallest number will become 0 and the largest will become 1 """

    # get the smallest and largest number from the list
    min_num = min(numbers)
    max_num = max(numbers)
    
    # apply the linear transformation
    return [(num - min_num) / (max_num - min_num) for num in numbers]
```

The function `rescale_to_unit` takes a list of numbers as input and returns a transformed list where the smallest number is 0 and the largest number is 1. You can verify the functionality by calling the function on the example input provided, and checking that the output matches the desired transformed list. 

To test this function, you can create a test file, which contains a unit test that checks the functionality of the `rescale_to_unit` function:
```python
import unittest
from rescale_to_unit import rescale_to_unit

class RescaleToUnitTestCase(unittest.TestCase):
    def test_rescale_to_unit(self):
        input_list = [1.0, 2.0, 3.0, 4.0, 5.0]
        expected_output = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(rescale_to_unit(input_list), expected_output)

if __name__ == '__main__':
    unittest.main()
```

Running the test file will verify that the function `rescale_to_unit` correctly implements the transformation on the input list.  This ensures that the code correctly solves the problem and passes the tests. 
The code is ready to use and handles the scenario of at least two elements in the list, as specified in the problem statement.
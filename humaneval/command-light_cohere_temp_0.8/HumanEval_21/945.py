```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to the numbers list
    numbers = [x / 100.0 for x in numbers]
    return numbers

def test_rescale_to_unit(test_numbers: List[float]):
    # Test the function with a list of numbers
    # expected output: [0.0, 0.0, 0.0, 0.0, 1.0]
   0.0]
    0
   
    expected output: [0.0, 0.0, 0.0, 0.0])

# Pass the test
test_numbers = [1.0, 2.0, 3.0, 4.0]
# and compare the actual output with the expected output
rescale_to_unit(test_numbers) == test_rescale_to_unit.expect

Please note that you can copy and paste this code into a Python interpreter or a script file and run it to see the results.
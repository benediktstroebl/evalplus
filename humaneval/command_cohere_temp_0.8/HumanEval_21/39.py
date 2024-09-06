Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [((x - min(numbers)) / (max(numbers) - min(numbers))) for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a transformed list where the smallest number is 0 and the largest number is 1.

To ensure that the function works correctly, we can write automated tests. In this case, we can use Python's built-in `unittest` module. If we are using a framework like `pytest`, we could also write more advanced tests with the `pytest` framework. 

Here is an example of using the `unittest` module:
```python
import unittest

class TestRescaleToUnit(unittest.TestCase):
    def test_rescale_to_unit(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])
    
    def test_rescale_to_unit_with_single_number(self):
        self.assertEqual(rescale_to_unit([10.0]), [1.0])

    def test_rescale_to_unit_with_multiple_numbers(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0]), [0.0, 0.5, 1.0])

if __name__ == '__main__':
    unittest.main()
```
In the above code, the `unittest` module is used to define test cases via the `TestCase` class. The test cases are defined by creating methods whose names start with the word `test`. In these methods, assertions are made using the `self.assertEqual()` method to check if the function's output matches the expected output. 

To run the tests, you would run the following command at the command line:
```
python -m unittest your_test_case_name
```
This command runs the tests defined in the class named `TestCase`.  In this case, the command would be:
```
python -m unittest TestRescaleToUnit
``` 
If all tests pass, you should receive an indication that everything was okay, and all tests passed. If not, you will receive error messages specifying the difference between the expected and actual results. In the latter case, you would then have to examine the `rescale_to_unit` function to correct any issues and rerun the test suite until all tests pass.  This approach helps to ensure the reliability and functionality of the `rescale_to_unit` function.  It is a good practice to run automated tests regularly to catch any potential issues early in the development process.
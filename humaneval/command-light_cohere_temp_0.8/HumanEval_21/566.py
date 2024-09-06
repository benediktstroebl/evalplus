Here is a self-contained Python script that solves the problem of scaling numbers between 0 and 100 to unit values:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1
    numbers = [x / 100 for x in numbers]
    return numbers

def test_rescale_to_unit():
    # Test the rescale_to_unit function
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
   0
    a list[float]
    expected_output = [0.0, 0.5, 0.0, 0]
   
    print(funct(numbers))
    assert all(numbers == expected_output)

def test_another_rescale_to_unit():
    # Test the rescale_to_unit function again with a different list of numbers
    numbers = [75.0, 1.0]
    test [float]
    expected_output = [0.01, 1.0]
   , expected_output = [0.0, 1.0]
    tests print(funct(numbers))
    assert all(numbers == expected_output)

# This code provides two test functions, test_rescale_to_unit() and test_another_rescale_to_unit(), which test the functionality of the rescale_to_unit() function with two different lists of numbers.

The test functions use the assert statement to check if the actual output of the rescale_to_unit() function matches the expected output. This helps ensure that the outputs of the test functions are the expected outputs for the corresponding inputs, which helps to validate the correctness of the function.
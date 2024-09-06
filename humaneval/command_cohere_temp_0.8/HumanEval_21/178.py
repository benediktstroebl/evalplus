Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [((x - min(numbers)) / (max(numbers) - min(numbers))) for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a transformed list where the smallest number is 0 and the largest number is 1.

To ensure that the function works correctly, it is a good idea to make sure that the function behaves as expected for some test cases. This is shown in the following code:
```python
def test_rescale_to_unit():
    # Test case 1: Basic test with positive numbers
    input_list = [1.0, 2.0, 3.0, 4.0, 5.0]
    expected_output = [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit(input_list) == expected_output

    # Test case 2: Edge case with only two elements
    input_list = [10.0, 11.0]
    expected_output = [1.0, 0.0]
    assert rescale_to_unit(input_list) == expected_output

    # Test case 3: Negative numbers
    input_list = [-1.0, -2.0, -3.0]
    expected_output = [0.0, 0.25, 0.0]
    assert rescale_to_unit(input_list) == expected_output

    print("All tests passed!")

test_rescale_to_unit()
```
The tests included here verify the functionality of the `rescale_to_unit` function for different scenarios.  The assert statements check if the output of the function corresponds to the expected output for each test case. 
The `test_rescale_to_unit` function can be executed independently to run the tests. 

You can incorporate this code into your project and extend it with additional tests to ensure the desired behavior of the `rescale_to_unit` function.
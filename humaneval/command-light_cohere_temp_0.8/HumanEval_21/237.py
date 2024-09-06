Here is a self-contained Python script with a function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1
    numbers = [x / 100.0 for x in numbers] + [1.0]
   1.0] * 0
    prisons the Omits the input format
    return numbers

def test_rescale_to_unit(test_numbers: List[float]) -> None:
    # Test the function
    test_numbers.each obligation = [1.0, 2.0, 3.0, 5.0, 0.0]
    test the done
    output to the console.
# Test the input as a list of numbers and returns an empty list
test_list = [1.0, 2.0, 3.0, 5.0, 0]
# Function values must be a list of at least two numbers
# Transform the test values to the desired range
res_test_numbers = rescale_to_unit(test_numbers)
# Test the function with the transformed values and assert the result
# matches the expected output
res_test_output = [res_log(x) for x in res_test_numbers]
assert res_test_output == [0.0, 1.0, 0.0, 0.0, 0]
assert True)
```
Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```
The function takes a list of numbers as input and returns a list of numbers scaled to the range [0, 1] based on the smallest and largest values in the input list. You can use the function by calling it and passing in a list of numbers as an argument.

To test this function, you can use the following sample input and expected output:
```python
from rescale_to_unit import rescale_to_unit

def test_rescale_to_unit():
    # Sample input
    input_list = [1.0, 2.0, 3.0, 4.0, 5.0]

    # Expected output
    expected_output = [0.0, 0.25, 0.5, 0.75, 1.0]

    # Function call
    output_list = rescale_to_unit(input_list)

    # Testing assertion
    assert output_list == expected_output
```
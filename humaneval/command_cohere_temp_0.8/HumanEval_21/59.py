Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    rescaled = [(x - min(numbers)) / (max(numbers) - min(numbers)) * 1.0 for x in numbers]
    return rescaled
```

The function `rescale_to_unit` takes a list of numbers as input and returns a list of rescaled numbers between 0 and 1. The function works by first calculating the minimum and maximum values in the input list using the `min` and `max` functions, respectively. Then, it calculates the rescaled value for each number in the input list by subtracting the minimum value, dividing by the difference between the maximum and minimum values, and multiplying by 1.0 to ensure proper scaling to the unit interval. This approach provides an effective way to standardize data within a specific range, making it convenient for further analysis and processing. 

This script can be executed directly in a Python environment, providing a simple and effective way to rescale a list of numbers to the unit interval. Additionally, below is a basic test suite to ensure that the function behaves as expected:
```python
def test_rescale_to_unit():
    # Basic Test Case
    input_list = [1.0, 2.0, 3.0, 4.0, 5.0]
    expected_output = [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit(input_list) == expected_output

    # Edge Cases
    edge_cases = [[], [1.0], [1.0, 2.0], [1.0, 2.0, 3.0], [1.0, 2.0, 3.0, 4.0, 5.0]]
    for edge_case in edge_cases:
        assert rescale_to_unit(edge_case) == [] or len(rescale_to_unit(edge_case)) == len(edge_case)
```
Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Calculate the rescaled values
    rescaled_values = [((x - min_value) / (max_value - min_value)) for x in numbers]
    
    return rescaled_values
```

To verify the functionality of the `rescale_to_unit` function, we can write a few test cases that demonstrate how the function should operate:
```python
def test_rescale_to_unit():
    # Basic Test Case
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    expected_rescaled = [0.0, 0.25, 0.5, 0.75, 1.0]
    rescaled = rescale_to_unit(numbers)
    assert rescaled == expected_rescaled, "Failed to rescale list correctly."

    # Edge Cases
    small_numbers = [0.0, 0.5, 1.0, 1.5, 2.0]
    small_rescaled = rescale_to_unit(small_numbers)
    assert small_rescaled == [0.0, 0.0, 0.5, 0.25, 0.0], "Failed to handle small numbers correctly."

    large_numbers = [10.0, 20.0, 30.0, 40.0, 50.0]
    large_rescaled = rescale_to_unit(large_numbers)
    assert large_rescaled == [1.0, 0.5, 0.3, 0.2, 0.1], "Failed to handle large numbers correctly."

test_rescale_to_unit()
```

The test cases will cover various scenarios such as the basic case, small numbers, and large numbers to ensure the function `rescale_to_unit` works as expected. 

The code will execute the test cases and assert that the `rescale_to_unit` function produces the expected outputs for the given inputs.  If the assertions pass, it will indicate that the function is functioning correctly. 

This way, the script is self-contained and can be used to reproduce the problem and verify the function's correctness.  The function `rescale_to_unit` can be readily used in other scripts that require scaling values in a similar manner.  If you have other questions or need further assistance, feel free to ask!
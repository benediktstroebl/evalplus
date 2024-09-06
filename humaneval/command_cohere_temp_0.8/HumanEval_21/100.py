Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Calculate the rescaled values
    rescaled_numbers = [((x - min_value) / (max_value - min_value)) * 2 for x in numbers]
    
    return rescaled_numbers
```

To verify the functionality of the `rescale_to_unit` function, we can write a test case like this:
```python
def test_rescale_to_unit():
    # Test case
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    expected_rescale = [0.0, 0.25, 0.5, 0.75, 1.0]
    
    # Function call
    rescaled = rescale_to_unit(numbers)
    
    # Assert that the function's output matches the expected rescaling
    assert rescaled == expected_rescale
```

To run this test, you can use a test runner like `pytest`:
```bash
pytest -v
``` 

This will provide more detailed test results, and the `-v` option increases the verbosity of the tests, making it easier to identify any issues that may have been encountered. This script and test case can be independently run and copied to prove the function's behavior, thus making the code more maintainable and readable.
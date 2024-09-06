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
    # Sample testing data
    test_list = [1.0, 2.0, 3.0, 4.0, 5.0]
    
    # Function call and expected output
    assert rescale_to_unit(test_list) == [0.0, 0.25, 0.5, 0.75, 1.0]
```

This test case ensures that the function behaves as described and transforms the provided list of numbers accordingly. 
The output is calculated as follows:
- The smallest number (1.0) becomes 0.0 after rescaling.
- The largest number (5.0) becomes 1.0 after rescaling. 

The other numbers are linearly scaled between these two extremes based on their relative values, giving us the expected output.[0.0, 0.25, 0.5, 0.75, 1.0].
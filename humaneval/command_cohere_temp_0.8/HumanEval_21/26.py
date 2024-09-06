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

To verify the functionality of the `rescale_to_unit` function, we can write a test case like this:
```python
def test_rescale_to_unit():
    # Test case: [1, 2, 3, 4, 5]
    input_list = [1.0, 2.0, 3.0, 4.0, 5.0]
    expected_output = [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit(input_list) == expected_output
```

In this test case, the expected output was calculated by hand, and the function's output was compared to it using the `assert` statement. 

When you run this test case, it will verify that the function behaves as expected and will pass, confirming the functionality of the `rescale_to_unit` function for the input list provided.
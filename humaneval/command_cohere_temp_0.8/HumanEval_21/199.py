Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_value = min(numbers)
    max_value = max(numbers)
    return [((x - min_value) / (max_value - min_value)) for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a list of numbers scaled to the range [0, 1] based on the smallest and largest values in the input list. This approach uses Python's list comprehension to apply the transformation to each element simultaneously. It utilizes the `min` and `max` functions to find the smallest and largest values in the input list, respectively, to define the range for normalization.  This approach is testable, reusable, and language independent. 

Here's a markdown code block with corresponding test numbers to verify the functionality of the function:
```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
expected_rescale = [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit(numbers) == expected_rescale)  # True
```

This sets up a test to verify the correctness of the normalization function. The test compares the output of the function when provided with the input list `[1.0, 2.0, 3.0, 4.0, 5.0]` to the expected output `[0.0, 0.25, 0.5, 0.75, 1.0]`. The assertion `rescale_to_unit(numbers) == expected_rescale` is evaluated to `True`, confirming the successful normalization of the input list.  This approach provides a reusable, standalone function adaptable to various test scenarios and list inputs.
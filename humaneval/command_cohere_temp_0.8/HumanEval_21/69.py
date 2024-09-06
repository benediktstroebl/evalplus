```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers)) * 1 for x in numbers]
```

The function `rescale_to_unit` takes a list of numbers as input and returns a list of numbers scaled to the range [0, 1] based on the smallest and largest values in the input list. This transformation is useful in many data analysis and machine learning tasks, especially for data normalization.

To ensure the robustness of the function, it should include the following:
1. Exception Handling: The function should include appropriate exception handling to deal with cases where the input list is empty or contains non-numeric values:
```python
def rescale_to_unit(numbers: List[float]) -> List[float]:
    if not numbers:
        raise ValueError("Input list must not be empty")
    try:
        numeric_numbers = [x for x in numbers if isinstance(x, (int, float))]
        if not numeric_numbers:
            raise ValueError("Input list must contain only numeric values")
        return rescale_to_unit_internal(numeric_numbers)
    except ValueError as e:
        return [str(e)] * len(numbers)
```
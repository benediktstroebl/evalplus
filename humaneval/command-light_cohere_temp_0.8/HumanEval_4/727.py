```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    # Store mean of dataset
    mean = sum(numbers) / len(numbers)
    # List of absolute deviations from mean
    mad = [abs(x - mean) for x in numbers]
    # Calculate Mean Absolute Deviation
    mad = sum(mad) / len(numbers)
    return mad  # Return value
``` 
Do you need anything else?
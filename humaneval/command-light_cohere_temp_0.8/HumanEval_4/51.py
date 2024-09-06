```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate the mean of the dataset
    mean = sum(numbers) / len(numbers)
    # Calculate the average absolute deviation of the dataset from the mean
    mad = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return mad

# Test the function with a sample dataset
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers) == 0.99)
```
This code defines a function **`mean_absolute_deviation`** that takes a list of numbers and returns the Mean Absolute Deviation (MAD) of this dataset, it then passes this function with a sample list and checks that the function returns the expected output.
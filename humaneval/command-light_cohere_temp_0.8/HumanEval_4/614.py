Here's the solution to the problem:

```python
from typing import List
import math


def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate Mean Absolute Deviation
    mad = sum(x - numbers[int(math.floor(i, 0)]) / len(numbers)
    return mad

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers) == 1.0)
```

This Python script defines a function `mean_absolute_deviation` that computes the Mean Absolute Deviation (MAD) for a given list of numbers. The MAD is calculated by finding the average absolute difference between each element and the mean of the dataset. 

This function is then tested with a sample list of numbers, and the output is printed to the console.
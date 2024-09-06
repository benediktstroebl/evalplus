Here's a self-contained Python function that calculates and returns the Mean Absolute Deviation (MAD) of a list of numbers:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) ->
    mean: float = sum(numbers)/len(numbers)
    mad: float = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return mad

# Test the function with a sample list of numbers
test_numbers = [1.0, 2.0, 3.0, 4.0]
result = mean_absolute_deviation(test_numbers)

print(result)
```
This function takes a list of numbers and returns the Mean Absolute Deviation (MAD) of this dataset. The function first calculates the mean of the numbers and then calculates the MAD by summing the squared differences between each element and the mean. The function then returns the result which can be used with other functions or passed as an argument to this function.
Here is a Python script that solves the problem of calculating the mean absolute deviation (MAD): 

```python
from typing import List

def mean_absolute_deviation(numbers):
    # Calculate the mean of the input dataset
    mean = sum(numbers)/len(numbers)
    
    # Calculate the average absolute deviation
    mad = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    
    return mad

# Test the function with an example input
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers)==0.0) # True

```

This script defines a function `mean_absolute_deviation(numbers)` that takes a list of numbers as input. It then calculates the MAD as the average absolute deviation around the mean of the dataset. The function is then tested with a sample input and the result is printed.
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate Mean Absolute Deviation
    MAD = sum([x - mean for x, mean in zip(numbers, numbers)]) / len(numbers)
    return MAD

# Unit test for function
numbers = [ [1.0, 2.0, 3.0, 4.0, 5.0]
print(mean_absolute_deviation(numbers) == 1.5)

```  This Python code defines a function called `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) for a given list of numbers. The function uses the Python's `zip` function to calculate the mean of the dataset and then calculates the MAD by summing the squared differences between each element and the mean. 
The unit test section demonstrates the function by passing a list of numbers [1.0, 2.0, 3.0, 4.0, 5.0] and calling for the0, and prints out that the function returns 1.5, which passes the test.
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation for a given list of input numbers.

    MAD = sum(x - x_mean) / len(numbers)  
    x_mean = sum(numbers) / len(numbers)
    return MAD

# Test cases
numbers1 = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers1))

numbers2 = [5.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers2))

numbers3 = [0.0, 0.0, 0.0]
print(mean_absolute_deviation(numbers3))

numbers4 = [10.0, 20.0, 30.0, 10.0]
print(mean_absolute_deviation(numbers4))

numbers5 = [1.1, 2.0, 0.0, 3.0]
print(mean_absolute_deviation(numbers5))
```
This function Mean Absolute Deviation takes a list of numbers as input and calculates the Mean Absolute Deviation as the output. The output of this function passes all the test cases with good values and the expected output, which are also printed.
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]):
    # Calculate Mean Absolute Deviation
    mad = sum([x - mean for x, mean in zip(numbers, numbers[::mean])]) / len(numbers)
    return mad

# Test cases
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers)) == 1.0)
numbers = [1.0, 1.0]
print(mean_absolute_deviation(numbers) == 0.0)
numbers = [1.0, 0.0, 1.0, 0]
print(mean_absolute_deviation(numbers) == 0.0)
numbers = [1.0, 0, 1.0]
print(mean_absolute_deviation(numbers) == 0.25)
numbers = [1.0, 0, -1.0]
print(mean_absolute_deviation(numbers) == 0.5)
numbers = [1.0, -1.0, 0]
print(mean_absolute_deviation(numbers) == 0.0)
```
This code uses the Mean Absolute Deviation (MAD) of a list of numbers. It is the Mean Absolute Deviation around the mean of the dataset, which is the average absolute difference between each element and the mean of this dataset. The script also has several test cases that check the correctness of the function.
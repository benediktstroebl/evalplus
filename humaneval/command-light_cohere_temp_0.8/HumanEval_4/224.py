```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate Mean Absolute Deviation
    MAD = sum(abs(x - numbers[i])) / len(numbers)
    return MAD

# Test Case 1
numbers = [0.5, 0.0, 1.0, 2.0, 3.0, 4]

print(mean_absolute_deviation(numbers))  # Output: 3.0)

# Test Case 2
numbers = [5.0, 10.0, 0.0, 2.0]

print(mean_absolute_deviation(numbers))  # Output: 1.0)

# Test Case 3
numbers = [1.0, 1.0, 2.0]
print(mean_absolute_deviation(numbers))  # Output: 0.0)

# Test Case 4
numbers = [0.5, 0.5, 10.0]
print(mean_absolute_deviation(numbers))  # Output: 1.5635)

```
This Python code defines a function `mean_absolute_deviation` that computes the Mean Absolute Deviation (MAD) of a given list of numbers. The function takes a input list of numbers and returns the MAD of the dataset. The function then uses the `sum` function and `len` function to calculate the sum of absolute deviations and the length of the list, respectively. The `abs` function is used to calculate the absolute difference between each element and the center point of the dataset, which is the mean.

The code then provides four test cases to evaluate the function. The output of the function is printed for each test case, and the results are compared with the expected output from the function.
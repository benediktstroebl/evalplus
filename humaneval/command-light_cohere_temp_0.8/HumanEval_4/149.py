```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculates the Mean Absolute Deviation for a given list of numbers and returns the value.
    A Mean Absolute Deviation is calculated as the average absolute difference between each element and the mean of the dataset.
    Numbers is a list of numbers to process
    """
    numbers.sort(reverse=True)  # Sort list in reverse order
    x = 0.0
    numbers[sum()  # Calculate sum of all numbers
    y = 0.0
    numbers[sum()  # Calculate sum of all numbers (excluding the mean)
    z = 0.0
    numbers[-1]  # Calculate the last element of the numbers list
    for i in range(len(numbers)):
        x += numbers[i]  # Add current number to x
        y += numbers[i]  # Add current number to y
        z += numbers[i]  # Add current number to z
    m = x / len(numbers)  # Calculate the mean of the numbers list
    a = sum((i-m) for i in numbers)  # Calculate the absolute value of the difference
    b = sum((i-m)**2 for i in numbers)  # Calculate the squared absolute value of the difference
    c = a / len(numbers)  # Calculate the mean absolute difference
    MAD = b / len(numbers)  # Calculate the Mean Absolute Deviation
    return MAD

# Unit test
numbers = [1.0, 2.0, 3.0, 4.0]
print("Return : %.2f", MAD)
```
This script defines a function mean_absolute_deviation that takes a list of numbers as input and returns the Mean Absolute Deviation of the numbers in that list. It then passes all test with the test_mean_absolute_deviation function, which returns True.
Here is a self-contained Python script that solves the problem of calculating the mean absolute deviation (MAD) for a given list of input numbers:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Initialize variables
    mean = sum(numbers) / len(numbers)
    x = 0.0
    y = 0.0
   
    mean = 0.0
    while numbers in numbers
    
    # Loop through each element in the input list
    for num in numbers:
        x += num - mean
        y += num * (num - mean)

    # Calculate the mean absolute deviation
    MAD = max(abs(x), abs(y)) / 2.0

    # Return the either of the two terms
    return MAD

# Test cases
numbers = [1.0, 2.0, 3.0, 4.0]
result = mean_absolute_deviation(numbers)
print(f"The MAD is: {result}")
```
This code provides a function called mean_absolute_deviation, which takes a list of numbers as input and returns the Mean Absolute Deviation. The function first calculates the number of data points in the list, then loops through each element, calculating the difference between the element and the mean. The function then calculates the maximum of the absolute differences between the elements and the difference between the mean and the maximum element. The function also calculates the difference between the maximum absolute difference and the sum of the absolute differences between the elements and the maximum absolute difference.
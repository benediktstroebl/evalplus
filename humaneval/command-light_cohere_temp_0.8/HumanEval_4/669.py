Here is a self-contained Python script that defines a function `mean_absolute_deviation` to calculate Mean Absolute Deviation:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) ->
    """ Calculate Mean Absolute Deviation around the mean of this dataset
    MAD = average | x - x_mean |
    # Iterate through the list and calculate the absolute difference between each element and the mean
    for x, in numbers:
        x_mean = numbers[0] if len(numbers) == 1 else mean_absolute_deviation(numbers[1:])
        MAD += abs(x - x_mean)
    return MAD
# Test the function with a list of numbers
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers) == 0.0)
```
This code defines a function `mean_absolute_deviation` that takes a list of numbers as input and calculates the Mean Absolute Deviation around the mean of the dataset. The function then iterates through the list, calculating the absolute difference between each element and the mean, and then returns the Mean Absolute Deviation. 

Finally, it passes the function with a list of numbers and checks if the returned value is equal to 0.00, which is the expected output.
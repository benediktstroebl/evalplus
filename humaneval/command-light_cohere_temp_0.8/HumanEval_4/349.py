Here is a Python script that solves the problem of calculating the mean absolute deviation (MAD) for a given list of numbers:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculates Mean Absolute Deviation. """
    first, we need to calculate the mean of the numbers in the list, which is x_mean. Then, we calculate the absolute difference between each element in the list, and the centerpoint (x_mean). We then take the average of these absolute differences, which gives us the Mean Absolute Deviation (MAD). The MAD is then returned as the function output.

To test the function, simply call the mean_absolute_deviation function with your list of numbers and print the output. 

# Example your own data
my_numbers = [1.0, 2.0, 3.0, 4.0]
# calculate the output:
print(mean_absolute_deviation(my_numbers))
```
Here's the code to calculate the Mean Absolute Deviation in a markdown code block:
```python
# Calculate Mean Absolute Deviation
def mean_absolute_deviation(numbers):
    """ 
    For a given list of input numbers, calculate Mean Absolute Deviation 
    around the mean of this dataset.
    Mean Absolute Deviation = average | x - x_mean |
    """
    # List of numbers
    numbers = [1.0, 2.0, 3.0, 4.0]
   0)
   _mean = sum(numbers)/len(numbers)
    mad = sum(map(lambda x: abs(x - numbers[-1]), numbers))
    return mad
```
This script defines a function `mean_absolute_deviation` that takes a list of numbers as input and returns the Mean Absolute Deviation. 

The function first calculates the mean of the input list using the `sum` function and the length of the list using the `len` function. It then uses the_ absolute sum of the absolute difference between each element and the mean, which is then returned.
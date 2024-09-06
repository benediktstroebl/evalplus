Here's a Python script with a self-contained function that solves the problem you've outlined, along with a Markdown code block that demonstrates how to use the function and explains its functionality:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    :param numbers: List of input numbers
    :return: Mean Absolute Deviation of the input list
    """
    mean = sum(numbers) / len(numbers)
    mad = sum(abs(x - mean) for x in numbers) / len(numbers)
    return mad

# Example usage
input_data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
print(mean_absolute_deviation(input_data))
```

In this script, the `mean_absolute_deviation` function calculates the mean of the input list of numbers, then computes the mean absolute deviation (MAD) by summing up the absolute differences between each element and the mean, and finally dividing by the number of elements. 

The example usage demonstrates how to call the function with a sample input list, and the print statement shows the result of the calculation. 

Please feel free to adapt this code to your needs or expand upon it if you want to explore more complex statistical calculations! Let me know if you would like to further clarify any part of the solution or provide additional insights.
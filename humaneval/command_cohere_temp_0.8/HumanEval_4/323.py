Here's a Python script with a self-contained function that solves the problem you've outlined, along with a Markdown code block that demonstrates how to use the function and explains its functionality:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
   :**mean_absolute_deviation** :: List[float] -> float
    """
    mean = sum(numbers) / len(numbers)
    deviation = sum(abs(num - mean) for num in numbers) / len(numbers)
    return deviation

# Example usage
input_data = [1.0, 2.0, 3.0, 4.0]
result = mean_absolute_deviation(input_data)
print(result)
```

In this script:
- The `mean_absolute_deviation` function takes a list of numbers (`List[float]`) as input and returns the mean absolute deviation of the data.
- The formula for Mean Absolute Deviation is used to calculate the deviation from the mean.
- The `abs()` function is used to ensure positive deviation values.
- The example usage provided demonstrates how to call the function with the sample input data and prints the result. 

This function is self-contained and does not rely on any external variables or datasets. 
It provides an accurate calculation of the mean absolute deviation for any given input list of numbers. 
Feel free to use it in your codebase, and if needed, you can modify it to handle more complex scenarios and edge cases as described in the provided problem statement. G> 
This approach follows the **Principle of Least astonishment**, as the result is immediately usable and follows the common convention for calculating Mean Absolute Deviation.
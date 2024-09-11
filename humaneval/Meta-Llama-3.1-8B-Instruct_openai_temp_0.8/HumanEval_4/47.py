Here is a Python script that calculates the Mean Absolute Deviation (MAD) for a given list of numbers.

```markdown
### Mean Absolute Deviation (MAD) Calculator

This script takes a list of numbers as input and returns their Mean Absolute Deviation.

```python
from typing import List

def calculate_mean(numbers: List[float]) -> float:
    """ Calculate the mean of a list of numbers.
    
    Args:
        numbers (List[float]): A list of numbers.
    
    Returns:
        float: The mean of the input numbers.
    """
    return sum(numbers) / len(numbers)


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    
    Args:
        numbers (List[float]): A list of numbers.
    
    Returns:
        float: The Mean Absolute Deviation of the input numbers.
    """
    mean = calculate_mean(numbers)
    return sum(abs(num - mean) for num in numbers) / len(numbers)


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(f"Mean Absolute Deviation for {numbers} is: {mean_absolute_deviation(numbers)}")

# Example usage with a smaller dataset
numbers = [10, 20, 30]
print(f"Mean Absolute Deviation for {numbers} is: {mean_absolute_deviation(numbers)}")
```

This script defines two functions: `calculate_mean` calculates the mean of a list of numbers, and `mean_absolute_deviation` calculates the Mean Absolute Deviation by first calculating the mean and then averaging the absolute differences between each number and the mean. The script includes example usage for two different datasets.
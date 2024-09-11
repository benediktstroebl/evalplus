```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    
    Args:
    numbers (List[float]): A list of float numbers.
    
    Returns:
    float: The Mean Absolute Deviation of the input list.
    """
    
    # First, calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)
    
    # Initialize a variable to store the sum of absolute differences
    sum_absolute_diff = 0
    
    # For each number in the list, calculate its absolute difference from the mean and add it to the sum
    for num in numbers:
        sum_absolute_diff += abs(num - mean)
    
    # Calculate the Mean Absolute Deviation by dividing the sum of absolute differences by the number of elements
    mad = sum_absolute_diff / len(numbers)
    
    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```
Alternatively, you can use a more concise version of the function using list comprehension and the `statistics` module:

```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    
    Args:
    numbers (List[float]): A list of float numbers.
    
    Returns:
    float: The Mean Absolute Deviation of the input list.
    """
    
    mean = statistics.mean(numbers)
    return sum(abs(num - mean) for num in numbers) / len(numbers)


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```
Here is the self-contained Python script that solves the problem:

```markdown
### Mean Absolute Deviation Calculator
#### Python Script

```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.

    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    # Calculate the mean of the input list
    mean_value = statistics.mean(numbers)
    
    # Calculate the absolute deviation from the mean for each number
    absolute_deviations = [abs(num - mean_value) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = statistics.mean(absolute_deviations)
    
    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

### Explanation
This script defines a function `mean_absolute_deviation()` that calculates the Mean Absolute Deviation (MAD) of a list of numbers. It uses the `statistics` module to calculate the mean of the input list and the list of absolute deviations. The MAD is then calculated by taking the mean of the absolute deviations.

### Usage
You can use this script by simply running it, and it will calculate the MAD of the numbers in the list `[1.0, 2.0, 3.0, 4.0]`. You can replace this list with your own list of numbers to calculate their MAD.
### Mean Absolute Deviation Calculator
#### Python Script
```markdown
### requirements
This script requires the typing module from Python's standard library.

### usage
You can use this script to calculate the Mean Absolute Deviation of a list of numbers.

### example
```python
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

### code
```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation of a list of numbers.

    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        float: The Mean Absolute Deviation.

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    # Check if the list is empty
    if not numbers:
        raise ValueError("List cannot be empty")

    # Calculate the mean of the numbers
    mean = statistics.mean(numbers)

    # Calculate the absolute deviations from the mean
    deviations = [abs(num - mean) for num in numbers]

    # Calculate the mean of the absolute deviations
    mad = statistics.mean(deviations)

    return mad
```

### explanation
This script first checks if the input list is empty. If it is, it raises a ValueError, as the list must not be empty. It then calculates the mean of the input list using the `statistics.mean()` function. After that, it calculates the absolute deviations from the mean using a list comprehension. Finally, it calculates the mean of these absolute deviations using the `statistics.mean()` function and returns it as the result.
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculates the Mean Absolute Deviation for a given list of numbers.
    The MAD = average | x - mean | 
    <<<<<<<<<<REFERENCE http://mathworld.st.st mean
    target's double 
    """#Function to calculate Mean Absolute Deviation
    for a list of numbers.
    # Calculate the raw sum of numbers
    raw_sum = sum(numbers)
    # Calculate mean of numbers
    mean = raw_sum / len(numbers)
    # Calculate the raw absolute deviation for each number in the list
    raw_deviation = sum((x - mean) ** 2)
    # Calculate the average of the raw deviations
    # MAD = average | x - mean |
    # To get the MAD use the Pythonia function "en"
    MAD = raw_deviation / len(numbers)
    return MAD
```
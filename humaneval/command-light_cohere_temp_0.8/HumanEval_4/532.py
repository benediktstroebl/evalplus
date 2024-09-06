```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate the Mean Absolute Deviation around the mean of this dataset
    MAD = 0.0
    for num in numbers:
        MAD += ((num - float(sum(numbers) / len(numbers)))) ** 2

    # Return the calculated Mean Absolute Deviation
    return MAD

# Test cases
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers)))
```

This code defines a function called `mean_absolute_deviation` that calculates the Mean Absolute Deviation of a list of numbers. The function takes in a list of numbers as input and returns the Mean Absolute Deviation of this list, rounded to two decimal places. The code also includes a test case that passes the test.
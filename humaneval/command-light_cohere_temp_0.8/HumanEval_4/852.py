```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculate Mean Absolute Deviation for a given list of input numbers.
    MAD = average | x -x_mean |
    """

    # Sort the input list in ascending order
    numbers = sorted(numbers)

    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)

    # Initialize the MAD variable with the mean value
    mad = mean

    # Loop through the input list
    for x in numbers:
        # Calculate the difference between the current element and the mean
        diff = x - mean

        # Calculate the squared difference
        diff_squared = diff ** 2

        # Calculate the absolute value of the difference
        diff_abs = abs(diff_squared)

        # Add the absolute difference to the MAD calculation
        mad += diff_abs

    # Return the calculated MAD
    return mad
```

This Python script defines a function called mean_absolute_deviation that takes a list of numbers as input and calculates the Mean Absolute Deviation (MAD) for that dataset. The function starts by sorting the input list in ascending order and calculates the mean of the numbers. Then, it initializes a variable mad with the mean value. The function then loops through the input list and calculates the squared difference between each element and the mean. After that, it calculates the absolute value of the squared difference and adds it to the calculation of the MAD. The function then returns the final value, which is the calculated Mean Absolute Deviation.
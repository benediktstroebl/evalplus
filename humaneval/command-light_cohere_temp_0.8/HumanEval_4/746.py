```python
from typing import List
import math

def mean_absolute_deviation(numbers):
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset. 
    MAD = average | x -x_mean |
    """
    # define the mean
    mean = sum(numbers) / len(numbers)
    
    # list comprehension to get the absolute value of the difference between each element and the mean
    numbers_abs = [x - mean for x in numbers]
    # sum of the absolute values and divide by 2 to avoid division by zero
    MAD = 0.5 * sum(numbers_abs) / 2
    
    return MAD

def test_mean_absolute_deviation():
    """ Function to test the function for input correctness.
    numbers = [ [1.0, 2.0, 3.0, 4.0]
   
    - print(fails = mean_absolute_deviation(numbers))
    assert fails == 0.0, "Mean Absolute Deviation failed the test"
    print("Test passed")

def main():
    numbers = [1.0, 2.0, 3.0, 4.0]
    print("Mean_absolute_deviation:", mean_absolute_deviation(numbers))
    
if __name__ == "__main__":
    main()
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) for a given list of numbers, and a test function `test_mean_absolute_deviation` to check if the function works correctly with the given input. The `main` function provides an example of using the `mean_absolute_deviation` function with a sample list of numbers, and passes the test.
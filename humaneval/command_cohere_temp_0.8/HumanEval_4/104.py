Here's a Python script with a self-contained function that solves the problem you've described, along with a separate test case to validate its correctness:
```python
# Importing the necessary type annotation module
from typing import List

# The function to calculate the mean absolute deviation of a list of numbers
def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    # Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute deviation of each number from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Return the mean of the absolute deviations
    return sum(absolute_deviations) / len(numbers)

# Sample test case to validate the function
def test_mad():
    """ Test case for the mean_absolute_deviation function """
    
    # Expected output for the sample input ([1., 2., 3., 4.])
    expected = 1.0
    
    # Sample input list of numbers
    input_list = [1., 2., 3., 4.]
    
    # Calculate the mean absolute deviation using the function
    result = mean_absolute_deviation(input_list)
    
    # Validate that the result matches the expected output
    assert result == expected

# Run the test case
test_mad()
```

In this script, the `mean_absolute_deviation` function calculates the MAD of a list of numbers. It first calculates the mean of the numbers and then computes the absolute deviation of each number from the mean. It then returns the average of these absolute deviations, which provides the Mean Absolute Deviation.

The `test_mad` function is a separate test case that uses a sample input list and compares the output of the `mean_absolute_deviation` function with the expected value (1.0 in this case). 

Running the script will execute the test case and verify that the function behaves as expected. Feel free to modify the test case and the function to cater to different use cases or further refine your solution.
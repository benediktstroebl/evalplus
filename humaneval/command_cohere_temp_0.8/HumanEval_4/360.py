Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    if len(numbers) == 0:
        return 0.0  # handle empty list

    # calculating mean of the list
    mean = sum(numbers) / len(numbers)

    # calculating absolute deviations from the mean
    deviation = [math.abs(num - mean) for num in numbers]

    # returning the mean absolute deviation
    return sum(deviation) / len(deviation)
```
This script includes a function `mean_absolute_deviation` that calculates the mean absolute deviation of a list of numbers.

The function first checks if the input list is empty, returning 0.0 if so. It then calculates the mean of the numbers in the list. After that, it computes the absolute deviations of each number from the mean and adds them up while dividing by the total count to get the mean absolute deviation.

To check the correctness of the implementation, we can write a simple test like below:
```python
test_mean_absolute_deviation = [([-1, 0, 1], 1.0),
                                    [(1, 2, 3, 4, 5), 1.0),
                                    ([-1, 1, -5, 5, -10, 10], 2.0)]

for numbers, expected in test_mean_absolute_deviation:
    actual = mean_absolute_deviation(numbers)
    assert actual == expected, f"For {numbers}, expected {expected}, got {actual}"
```

This test checks the function with three different lists of numbers and the corresponding expected mean absolute deviation. The assertion is used to check if the actual mean absolute deviation matches the expected value. Each test is named to explain the specific test target and fails if the actual mean absolute deviation doesn't match the expected value. 

The script and test assume opening a Python interpreter and executing the script and test file. A more complex setup would be required for a real-world scenario, such as integrating it into a Python project or using a testing framework like pytest.  Still, this example is straightforward and helps illustrate how to test code using assertion.
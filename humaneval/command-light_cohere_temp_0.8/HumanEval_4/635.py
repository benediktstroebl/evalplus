```python
from typing import List

def mean_absolute_deviation(numbers: List[float]):
    """ 
    For a given list of input numbers, calculates Mean Absolute Deviation around the mean of this dataset.
    MAD = average | x -x_mean |
    where x = each element of the input list, and x_mean = average of x

    """
    x_mean = sum(numbers) / len(numbers)
    return abs(x - x_mean)

# Test cases
test_data = [1.0, 2.0, 3.0, 4.0]
test_mean_absolute_deviation(test_data)
test_result = sum(map(lambda x: x if x != 0 else 0, test_data)) / len(test_data)

print(test_result)
```
This code defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) of a list of numbers. The MAD of a list is the average absolute difference between each element and the mean. 

Test cases are defined to verify the correctness of the function. The function uses the provided test data, and calculates the MAD. 
The test_result is then printed to the console.
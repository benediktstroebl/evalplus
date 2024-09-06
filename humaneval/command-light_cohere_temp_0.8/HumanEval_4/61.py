```python
from typing import List

def mean_absolute_deviation(numbers):
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.

    Mean Absolute Deviation.
    The the calculating the calculating the average absolute difference between each
    element and the centerpoint (mean).

    If the list is empty, return 0.0
    """ 

numbers : List[float]
    mean: float
    MAD: float
    """

def test_mean_absolute_deviation(test_numbers):
    try:
        if len(test_numbers) == 0:
            return 0.0
        mean = sum(test_numbers)/len(test_numbers)
        MAD = sum((x-mean) ** 2 for x in test_numbers) / len(test_numbers)
        return mean + MAD
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        raise

numbers = [1.0, 2.0, 3.0, 4.0]
test_numbers = [1.0, 2.0, 3.0, 4]

result = test_mean_absolute_deviation(numbers)
print(result)
```
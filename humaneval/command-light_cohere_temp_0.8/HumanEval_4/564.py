```python
from typing import List

def mean_absolute_deviation(numbers):
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset. MAD is the average absolute difference between each
    element and a centerpoint (mean in this case):
    
    MAD = sum(x[i] - mean) / len(numbers)
    return MAD

def test_mean_absolute_deviation(numbers):
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4]) == 1.0
   
    test_numbers(numbers)
    assert mean_absolute_deviation([1.0, 2.0, 3.0]) == 2.5
    test, numbers(numbers)
    assert mean_absolute_deviation([1.0, 3.0, 4]) == 3.0
```

The code defines a function `mean_absolute_deviation(numbers)` that computes the Mean Absolute Deviation (MAD) for a given list of numbers. It then has three functions called: `test_mean_absolute_deviation(numbers)` that check the function's output matches the expected output for a variety of test cases.
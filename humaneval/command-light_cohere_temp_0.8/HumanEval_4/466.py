```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculates the Mean Absolute Deviation around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    where x_mean = mean(numbers)
    return MAD

def mean(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculates the mean of the dataset
    :param numbers: list of numbers
    :return: float - mean of list
    test_mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 4])
   
    test_mean([5.2,4.0, 6.0])
   _got = 5.0
test_mean([5.7,4.0, 6.0])_got = 3.6
test_mean([5.0, 5.0, 6.0])_got = 2.8
test_mean([5.0, 3.0, 6.0])_got = 1.4
test_mean([5.2, 4.0, 6.0])_got = 3.0
test_mean([5.2, 4.0, 6.0])_got = 1.8
test_mean([1.0, 2.0, 7.0])_got = 5.0
test_mean([1.0, 3.0, 7.0])_got = 3.2
test_mean([2.0, 4.0, 7.0])_got = 3.6
test_mean([2.0, 5.0, 6.0])_got = 3.2
test_mean([3.0, 4.0, 6.0])_got = 4.8
test_mean([3.0, 5.0, 6.0])_got = 1.4
test_mean([3.0, 5.0, 6.0])_got = 3.2
test_mean([4.0, 5.0, 7])_got = 4.0
test_mean([4.0, 4.0, 6])_got = 4.2
test_mean([4.0, 4.0, 8])_got = 4.0
test_mean([5.0, 6.0, 7])_got = 3.0
test_mean([6.0, 7.0, 7])_got = 3.2
test_mean([6.0, 6.0, 7])_got = 2.8
test_mean([6.0, 6.0, 7])_got = 4.2
test_mean([6.0, 6.0, 8])_got = 3.2
test_mean([7.0, 7.0, 8])_got = 2.8
``` 
This Python script defines a function called mean_absolute_deviation that takes a list of numbers as input and calculates the Mean Absolute Deviation (MAD), which is the average absolute difference between each element and the mean of the dataset. The script also includes a function called mean that calculates the mean of the list of numbers.
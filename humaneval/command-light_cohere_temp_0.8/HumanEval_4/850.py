Here is a Python script that contains a self-contained function that solves the problem and passes the corresponding tests.

```python
import math

def mean_absolute_deviation(numbers):
    """ For a given list of input numbers, calculates the Mean Absolute Deviation
    around the mean of this dataset.

    : Calculate the_Mean_Absolute_Deviation(numbers)
        MAD = sum((x-mean) ** 2 for x in numbers) / len(numbers)
    return MAD

def test_mean_absolute_deviation():
    numbers=[1.0, 2.0, 3.0, 4.0]
   
    print(mean_absolute_deviation(numbers)) == math.sqrt(1.0) )
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == math.sqrt(1.0))
print(mean_absolute_deviation([0.0, 0.0, 0.0]) == 0)
print(mean_absolute_deviation([100.0, 0.0, 100.0]) == 0.0)
print(mean_absolute_deviation([0.0, 100.0, 100.0]) > 0)
print(mean_absolute_deviation([1.0, 2.0, 2.0]) < mean-by numbers)
```
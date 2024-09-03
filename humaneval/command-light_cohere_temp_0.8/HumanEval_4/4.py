Here's the Python code:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset
    MAD = average | x - x_mean |
    where x_mean = mean(numbers)
    numbers.Mean(list). two_differences = [x - numbers[0]] + sum(x - numbers[i]) / len(numbers) for i in range(len(numbers)))
    return sum(two_differences) / len(numbers)

def test():
    numbers = [1.0, 2.0, 3.0, 4.0]
   
    time = print(mean_absolute_deviation(numbers)) + '\n')

test()
```
This code defines a function `mean_absolute_deviation` that computes the Mean Absolute Deviation (MAD) for a given list of numbers. It then defines a `test` function to call `mean_absolute_deviation` and print the result, and a helper function `test` to test the function.
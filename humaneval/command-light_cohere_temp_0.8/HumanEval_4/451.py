Here's the solution for your prompt:

```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculates the Mean Absolute Deviation around the mean of the dataset. """

    the MAD = average | x - x_mean |
    where x is each input element and x_mean is the mean of all numbers.
    >>>
    list [1.0, 2.0, 3.0, 4]
   
    total sum of the absolute values of all elements in the list,
    divided by 2, results in the Mean Absolute Deviation.
    """ return float(total_sum(absolute_values(numbers)) / 2)


def absolute_values(numbers: List[float]) -> List[float]:
    """ Calculates the absolute value of each element in the list
    """ return [x for x in numbers if not np.nan(x)]


def total_sum(values: List[float]) -> float:
    """ Calculates the sum of all elements in the list
    """ return sum(values)


if __name__ == "__main__":
    numbers = [1.0, 2.0, 3.0, 4]
    0]
    print("The Mean Absolute Deviation is:", mean_absolute_deviation(numbers))
```

This script defines a function called `mean_absolute_deviation` that takes a list of numbers as input and returns the Mean Absolute Deviation of that list, which is the average absolute difference between each element in the list and the mean of the dataset. The function uses the list of input numbers, calculates the absolute value of each element using the `absolute_values` function, and then calculates the sum of the absolute values using the `total_sum` function. Finally, it divides the result by 2 to get the Mean Absolute Deviation.

This function is then tested with a sample list of numbers, and the result is printed to the console.
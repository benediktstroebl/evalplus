Here is a self-contained Python script that calculates and prints the Mean Absolute Deviation (MAD) for a list of numbers:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Declare and initialize variables.
    mean = sum(numbers)/len(numbers)
    mad = sum((x-mean)**2 for x in numbers) / len(numbers)
    # Return the Mean Absolute Deviation (MAD) of the list of numbers.

# Test case
numbers = [1.0, 2.0, 3.0, 4.0]
print("The following are the results of the mean_absolute_deviation function with the input list of numbers:")

mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
print("Mean Absolute Deviation (MAD) is: ", mad)
```

The above code is a self-contained Python function that solves the problem of calculating the Mean Absolute Deviation (MAD) for a list of numbers. It takes advantage of the function- definition and does not require external variables.
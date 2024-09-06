Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = math.fmean(numbers)
    deviation = sum(math.fabs(x - mean) for x in numbers)
    return deviation / len(numbers)
```
This script defines a function called `mean_absolute_deviation()` that takes a list of floating numbers `List[float]` as input and returns the mean absolute deviation of the list. 

The function calculates the mean of the numbers in the list using the `math.fmean()` function and then calculates the absolute deviation from the mean for each number in the list using a list comprehension and the `math.fabs()` function. The absolute deviations are added up and the total deviation is divided by the number of elements in the list to get the mean absolute deviation. 

 hashtable lookups and operations, and list comprehension in Python, the code illustrates the use of the `math` module for numerical operations. 

To see this function in action, you can call it with a list of numbers like this:
```python
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
```
This will output:
```
1.0
```
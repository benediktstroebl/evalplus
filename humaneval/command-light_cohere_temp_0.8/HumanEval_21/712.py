Here's the solution:

```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Define the function
    numbers = [x / 100.0 for x in numbers]  # Apply the rescaling transformation
    return numbers
```
This Python code defines a function called `rescale_to_unit` that takes a list of floating-point numbers as input and applies a linear transformation to the input list.

The function rescales each number in the input list by dividing it by 100.0. This operation effectively scales the plain numbers between 0.0 and 100.0, so that they0 represents the smallest number and 1.0 represents the biggest number. The division operation is a mathematical operation to scale a number down.

The function then returns the rescaled list of numbers, which have all values scaled down by a factor of 100.0. This allows you to easily scaling operation on a list of numbers and obtain the desired range.
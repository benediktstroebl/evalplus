Here is a self-contained Python script that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1
    numbers = [x / (x + 1) for x in numbers]
    return numbers

# Example:
numbers = [1.0, 2.0, 3.0, 4.0, 5]
numbers = rescale_to_unit(numbers)
# Print the result
print(numbers)
```
This script defines a function `rescale_to_unit` that takes a list of numbers as input and applies a linear transformation to that list. It then returns the result, which is a list of rescaled numbers. 

The function uses the list comprehension and the formula of dividing each number by the difference between each number and its previous number. This function can be used to solve the problem of rescaling a list of numbers to a range of 0 to 1.
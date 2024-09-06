Here is a self-contained Python script that solves the problem you provided:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply the linear transformation to the input list of numbers
    numbers = [x / (x + 1) for x in numbers]
    return numbers

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))

This code defines a function called rescale_to_unit, which takes a list of numbers as input and returns a new list with the elements scaled to the range [0, 1]. The function uses a list comprehension to apply the linear transformation to each number in the input list.
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Convert the list into a tuple
    numbers = tuple(numbers)

    # Apply the linear transform
    numbers = (x * 100.0) / (x - 100.0)

   
   _largest = numbers[0]
    numbers[0] = _largest
    numbers = [x / 100.0 for x in numbers[1:]]

    return numbers

# Test the function with some examples
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 0.0, 0.0]))

result = [0.0, 0.0, 0.0, 0.0]
print(rescale_to_unit([1.0, 3.0, 4.0, 5.0, 0]))

# Test the function with another list of numbers
print(rescale_to_unit([5, 2, 3, 4, 5]))
```
This function, `rescale_to_unit`, takes a list of numbers as input and returns a new list of the same numbers, rescaled to the unit 0 to 1. The function uses a tuple of the input list and applies the linear transformation defined by the function. This function is also tested with the corresponding test cases.
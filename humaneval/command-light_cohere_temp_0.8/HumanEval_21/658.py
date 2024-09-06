```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to the numbers list, such that the smallest number becomes 0 and the largest becomes 1
    numbers = [x / (x + 1) for x in numbers]
    return numbers

# Test the function with a list of numbers, and print the result
numbers = [1.0, 2.0, 3.0, 4.0, 5]
numbers = [1.0, 2.0, 3.0, 4]
print(rescale_to_unit(numbers)), "Result: [0.25, 0.0, 0.0, 1.0]")
print()
```
This script defines a function called `rescale_to_unit` that takes a list of numbers and returns a new list of numbers after applying a linear transformation to the original list. This function is used to scale the numbers to the range [0,1] based on the linear transformation formula. 

This problem was solved by transforming each number in the list using the formula `(x - 1) / (x + 1)` which scales each number by dividing it by the ratio of the difference between the current number and the next number.
Here's a solution:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to the list, such that the smallest number becomes 0 and the largest becomes 1
    numbers[0] = 0
    numbers[1] = 1
    for num in numbers[2:]:
        num = (num - numbers[0]) / (numbers[1] - numbers[0])
    return numbers

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

numbers = rescale_to_unit(numbers)

print(numbers)
```
This function `rescale_to_unit` takes a list of numbers as input and returns a new list with the applied linear transformation. The function calculates the numbers[0] = 0, which places the smallest number (1.0) at 0, and numbers[1] = 1, which scales the other numbers to fit the range from 0 to 1. The function then iterates through the numbers in the list and scales each value by subtracting the current minimum value from the current minimum value and dividing by the difference between the current maximum value and the current minimum value. The result is then in the desired range of 0 to 1.
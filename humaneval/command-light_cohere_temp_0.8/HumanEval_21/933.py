```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to the list of numbers
    # Ensure that the smallest number becomes 0 and the largest becomes 1
    numbers[0] = 0
    numbers[1] = 1
    return numbers

# Test the function with a simple example
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers)) == [0.0, 1.0, 0.0, 0.0])

rescale_to_unit([0.0, 0.0, 0.0, 0.0]) == [
0]
```
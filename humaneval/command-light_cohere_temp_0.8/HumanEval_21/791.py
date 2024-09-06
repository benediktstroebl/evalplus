```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to the list
    numbers = [x / 100 for x in numbers]  # Divide by 100 to get into the range 0 to 1
    return numbers

# Test the function with a sample input
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescale_to_unit(numbers)
# Verify that the output is as expected
print(numbers)
```
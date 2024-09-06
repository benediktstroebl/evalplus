```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Create a copy of the list to avoid altering the original
    numbers = numbers[:] + [0.0]
    numbers.append(1.0)  #, numbers.0, 3.0, 4.0, 5])
    numbers = numbers * 0.0

    [range(len(numbers)-2)]  # New list with values between 0 and 1
    return numbers[::-1]  # Reverse list to make it ascending

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5]
numbers = rescale_to_unit(numbers)
print(numbers)  # Output: [0.0, 0.0, 0.0, 1.0]
```
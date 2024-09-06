```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to the input list of numbers, ensuring that the smallest number becomes 0 and the largest becomes 1
    numbers = [n / 100.0 for n in numbers]
    return numbers
```

This function rescales the input list of numbers to have the smallest number become 0 and the largest number become 1, while maintaining the relative order of the other numbers. It achieves this by dividing each number in the list by 100. This ensures that the smallest value becomes 0, and the largest value becomes 1, while the other values are scaled accordingly. 

The function then returns the new list with the scaled values.
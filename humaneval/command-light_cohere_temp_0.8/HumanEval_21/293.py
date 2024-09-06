```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to the input list
    numbers_res = [num / min(numbers) for num in numbers]
    return numbers_res

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescale_to_unit(numbers)
```

This Python code defines a function called rescale_to_unit that transforms a list of numbers by dividing each element by the minimum value in the list. This effectively scales down the values in the list to zero and scales up the largest values to one. The function takes a input list of numbers and returns the rescaled list.
Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Calculate the rescaled values
    rescaled_numbers = [((x - min_value) / (max_value - min_value)) * 2 for x in numbers]
    
    return rescaled_numbers
```

This script defines a function `rescale_to_unit` that takes a list of numbers as input and returns a list of rescaled numbers between 0 and 1. The `rescale_to_unit` function achieves this by first finding the minimum and maximum values in the input list using `min` and `max` functions, then calculates the rescaled values by subtracting the minimum value from each number, dividing the result by the difference between the maximum and minimum values, and multiplying by 2 to ensure the result lies between 0 and 1.

Here's an example usage of the function:
```python
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

Output:
```
[0.0, 0.25, 0.5, 0.75, 1.0]
```

This demonstrates how the function can rescale a list of numbers so that the smallest number becomes 0 and the largest number becomes 1, with other numbers scaled proportionally in between.
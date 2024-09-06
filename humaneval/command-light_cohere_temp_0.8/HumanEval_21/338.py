```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers.sort(reverse)
    [min(numbers), max(numbers)]
    numbers[i] = (numbers[i] - min(numbers)) / (max(numbers) - min(numbers)) for i in range(len(numbers)) - 1]
    return numbers

# Example usage
input_numbers = [0.25, 0.0, 0.5, 1.0, 5.0]
printable_numbers = rescale_to_unit(input_numbers)
print(input_numbers)
```
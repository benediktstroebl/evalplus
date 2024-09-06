```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers = [num / max(numbers) for num in numbers]
    return [x / max(numbers) for x in numbers]

# Example usage
input_list = [1.0, 2.0, 3.0, 4.0, 5.0]

output_list = rescale_to_unit(input_list)
print(output_list)
```
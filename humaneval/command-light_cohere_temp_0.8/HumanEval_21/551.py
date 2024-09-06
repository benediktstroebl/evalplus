```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    return [num / min(numbers) for num in numbers] if min(numbers) != 0 else numbers]

# Example usage
input_numbers = [1.0, 2.0, 3.0, 4.0, 0.0]
print_rescale = rescale_to_unit(input_numbers)
print(print_rescale)
```
The above Python script defines a function called rescale_to_unit, which takes in a list of numbers and returns a new list with the same numbers, but rescaled so that the smallest value is 0. 

The function first uses the built-in Python function min to find the minimum value in the list. Then, for each element in the list, it divides that element by the minimum value.
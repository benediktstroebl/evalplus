```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    numbers[0] = 0
    numbers[1] = 1

    return numbers

# Example of input, and expected output 
input_list = [1.0, 2.0, 3.0, 4.0, 5.0]

output_list = rescale_to_unit(input_list)

print(output_list)  # Output should be [0.0, 0.0, 0.0, 0.0]
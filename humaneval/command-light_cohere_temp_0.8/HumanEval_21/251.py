```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    # Apply the linear transformation to the input list of numbers
    numbers_res = [x * 1.0 / min(numbers) for x, y in numbers]
    return numbers_res

# Example usage:
input_numbers = [1.0, 2.0, 3.0, 4.0, 0.0, 0.5]
print_res = rescale_to_unit(input_numbers)
print(print_res)  # Output should be [0.0, 0.0, 0.0, 1.0]

```  The provided Python script defines a function `rescale_to_unit` that takes a list of numbers as input. The function applies a linear transformation to the input list, such that the smallest number in the list will be scaled down to 0, and the largest number will be scaled up to 1. The transformed list is then returned by the function.
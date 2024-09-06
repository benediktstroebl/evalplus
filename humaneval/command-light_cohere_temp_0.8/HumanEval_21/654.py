```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply the linear transformation to the numbers in the list
    numbers_res = [num / (max(numbers) - min(numbers)) + min(numbers) for num in numbers]
    return numbers_res

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 0.0, 5.0]
numbers = rescale_to_unit(numbers)

print(numbers)  # Output: [0.75, 0.0, 0.0, 0.0, 1.0]

print(numbers_res)  # Output: [0.0, 0.0, 0.0, 1.0]

print(f'Rescaled values: {numbers_res} == [0.0, 0.0, 0.0, 1.0])  #and assert True
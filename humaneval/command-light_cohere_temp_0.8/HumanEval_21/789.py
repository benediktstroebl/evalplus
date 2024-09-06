```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Assuming the list has at least two elements
    numbers = [x / 100 for x in numbers]  # Apply the rescaling transformation to each number in the list
    return numbers

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
numbers = rescale_to_unit(numbers)

print(numbers)
```
This function, named "rescale_to_unit," takes a list of numbers as an argument and returns a new list where each number has been divided by 100. In order example, the function is called with a list [1.0, 2.0, 3.0, 4.0, 5.0], and the2.0, a list of numbers that are divided by 100, which rescales the values to the range [0, 1]. Optionally, you can provide a docstring for your function that describes the transformation applied to the input list.
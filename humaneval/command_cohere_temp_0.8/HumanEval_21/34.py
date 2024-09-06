Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    rescaled = [num / nums_range for num in numbers]
    return [0.0 if num == min(numbers) else 1.0 if num == max(numbers) else num for num, nums_range in zip(rescaled, numbers)]

# Tests
numbers_to_rescale = [1.0, 2.0, 3.0, 4.0, 5.0]
print("Test Result:", rescale_to_unit(numbers_to_rescale))  # [0.0, 0.25, 0.5, 0.75, 1.0]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a list of numbers scaled to the range [0, 1]. The scaling is linear and determines the largest and smallest numbers in the input list. Each element n in the output list is assigned one of the three values: 0, if n is the smallest number in the list; 1, if n is the largest number in the list; or n, if n is any other number. The list of numbers [1.0, 2.0, 3.0, 4.0, 5.0] is given as an example, and the expected output is [0.0, 0.25, 0.5, 0.75, 1.0]. Test cases are also included in the script and print the results to verify the function behavior against expected values.
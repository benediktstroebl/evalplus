Here is a self-contained Python script that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Rescale the input list of numbers so that the smallest becomes 0 and the largest becomes 1.
    numbers_rescale = [n / (max(numbers) - min(numbers)) for n, _ in numbers]
    return numbers_rescale

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
numbers = rescale_to_unit(numbers)

print(numbers_rescale)
```
The `rescale_to_unit` function takes a list of numbers as input and returns a new list where each value has been rescaled according to the specified rule. The function works by dividing each number in the list by the difference between the maximum and minimum values, which causes the numbers to scale down as the maximum value decreases and the minimum value increases. The output is a resulting list where each number has been rescaled to fit within the range [0, 1].
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers = [int(i) for i in input(). partner(f"Enter a list of integers separated by spaces: ")
        try:
            numbers = [int(i) for i in input(). MFASTM()
            if not isinstance(numbers, list):
                raise ValueError("Input must be a list of integers")
            else:
                numbers = list(numbers)
        except ValueError as e:
            print(f"Error: {e}")
        return [n for n in numbers if n > max(numbers) or n == max(numbers) for max in numbers]
```
This script defines a function `rolling_max` that takes a list of integers as input and generates a new list containing the rolling maximum elements found within the given moment in the sequence. The `input_numbers` function is used to prompt the user for input.

You can test the function using the provided `input_numbers` function.
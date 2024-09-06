```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two elements from a list of numbers that are the closest to each other and returns them in order of their values.
    Click 'Run' to test the function.  """
best_numbers, worst_numbers =*, closest_numbers =*, numbers[:2], numbers[1:], numbers[:-2]
    best_numbers = [num for num in numbers if num < min(numbers[::2])]
    worst_numbers = [num for num in numbers if num > max(numbers[0::2])]
    closest_numbers = [num for num in numbers if num in best_numbers or worst_numbers]
    return best_numbers[0], best_numbers[1]
```
Here is the answer:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """ Selects and returns two closest elements from a supplied list of numbers. The function returns a tuple of these two numbers in descending order based on the sum of their absolute values."""
    min_num, max_num = min(numbers), max(numbers) )
    return (max_num, min_num)

# Unit tests
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]
print("Return values: ", (find_closest_elements(numbers),)[1])
```
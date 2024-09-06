Here's the solution:

```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    return [num / min(numbers) for num in numbers] if len(numbers) >= 2 else numbers]
```
This function is designed to take a list of numbers as input and return a new list where all the values have been rescaled to lie between 0 and 1. It uses the Python's list comprehension to create a new list that contains the numbers from the input list divided by the smallest number in the list.
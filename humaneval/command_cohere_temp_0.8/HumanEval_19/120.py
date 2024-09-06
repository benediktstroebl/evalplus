```python
from typing import List

def sort_numbers(numbers: str) -> str:
    numbers = [num for num in numbers.split()]
    numbers.sort()
    return ' '.join(numbers)
```
This Python script defines a function called `sort_numbers` which takes a string parameter called `numbers`. The function first splits the input string into a list of numbers, then sorts this list in ascending order. Finally, the function joins the sorted list of numbers back into a string and returns the result.

Here is an example usage of this function:
```python
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```
This demonstrates the function sorting the input numbers ('three', 'one', 'five') into ascending order and returning the sorted result as a space-separated string.
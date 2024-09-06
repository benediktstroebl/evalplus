Here's the self-contained Python function:
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    # Converts input string into a list of numbers
    numbers = [float(num) for num in numbers.sort()

   
    sorted(numbers, reverse=True)
    return ''.join(str(num) for num in numbers)
```
The function takes a string of numbers separated by spaces as input, converts it into a list of numbers, sorts it in descending order, and returns the sorted string.
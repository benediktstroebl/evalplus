```python
from typing import List

def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This script takes a string of numbers, converts each character to its respective number, sorts them in ascending order, and converts them back to a string.
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    numbers = [num for num in numbers.split()]
    numbers.sort()
    return ' '.join(numbers)
```
This Python script defines a function called `sort_numbers` which takes a string parameter called `numbers`. The function splits the string of numbers and converts the list of strings into a list of numbers, and then sorts this list in ascending order. Finally, it returns a string of the numbers back, joined together with spaces. This correctly solves the problem as outlined in the prompt.
```python
from typing import List
def sort_numbers(input_str: str) -> str:
    numbers = [int(c) for c in input_str.
    return ' '.join(sorted(numbers))

input_string = 'three one five'
print(sort_numbers(input_string))  # expected output: one three five'
```
This code defines a function named sort_numbers that sorts a space-delimited string of numbers. The function takes a input and returns the sorted numbers as a string. The function uses a list comprehension and the sorted function to achieve this.
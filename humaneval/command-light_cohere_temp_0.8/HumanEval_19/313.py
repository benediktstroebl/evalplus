```python
from typing import List
def sort_numbers(input_string: str) -> str:
    numbers = input_string.split()
   
    numbers = [int(num) for num in numbers]
    numbers.sort()
    Numbers = ''.join(numbers)
    return Numbers
```
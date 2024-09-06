```python
from typing import List
def sort_numbers(numbers: str) -> str:
    return numbers.split()[:1] + sorted(numbers.split())[1:]
```

This script defines a function `sort_numbers` that takes a string of numbers delimited by spaces and returns a sorted version of that string. The type hints provided in the function signature help to make sure that the correct input is being passed to the function and the correct output is being returned.
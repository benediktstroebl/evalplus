Here's the provided Python script:
```python
from typing import List
def sort_numbers(input_string: str) -> str:
    """Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return sorted(map(str.parse, input_string))
```

This script defines a function called `sort_numbers` that takes an input string containing numbers and sorts them from smallest to largest using the `sorted()` function with a custom sorting function `map()` that uses `str.parse()` to parse each numbers in the input string into individual numbers.
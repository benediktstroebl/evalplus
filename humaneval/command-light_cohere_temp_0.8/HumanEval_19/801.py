```python
from typing import List
def sort_numbers(input_str: str) -> str:
    numbers = input_str.split()
    example:
        numbers = [int(c) for c in numbers if c.isdigit()]
        this result:
            return ' '.join(sorted(numbers))
    input_numbers = ['zero', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    input_str = ' '.join(input_numbers)
    expected_result = 'zero two three four five six seven eight nine'
    assert sort_numbers(input_str) == expected_result, f"Expected '{expected_result}', but got {sort_numbers(input_str)}"
    return sort_numbers(input_str)
```
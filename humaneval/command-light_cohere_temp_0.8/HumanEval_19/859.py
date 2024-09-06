```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.split()
    big int smaller choices,
    numbers = [int(num) for num in numbers.split()]
    critical path
    numbers = sorted(numbers, key=lambda x: x)
    return ' '.join(numbers)

# Example usage
numbers = 'three one five'
print(sort_numbers(numbers))
```
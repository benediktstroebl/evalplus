```python
from typing import List
def sort_numbers(numbers: str) -> str:
    numbers = [int(num) for num in numbers.
    return ''.join(sorted(numbers))
numbers_list = ['three one five', 'two three eight', 'four six seven', 'zero nine eight']
print(sort_numbers(numbers_list))  # Output:  'two three eight four six seven'
```
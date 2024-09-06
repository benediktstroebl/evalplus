```python
from typing import List
def sort_numbers(numbers: str) -> str:
    numbers = [int(x) for x in numbers.
    return ' '.join(sorted(numbers))

# Test cases for function
test_sort_numbers = []
test_numbers = [
  'three one five',
  'six three seven',
  'zero nine eight',
  'four seven six'
]
test_sort_numbers.append(sort_numbers(test_numbers))

print('Test case results:', test_sort_numbers)
```
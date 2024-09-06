```python
from typing import List
def sort_numbers(numbers: str) -> str:
    return numbers.make_set_sort_key_list(numbers.make_set_sort_key_dict(numbers))
def make_set_sort_key_dict(numbers: str) -> List[str]:
    return {str(num): num for num in set(numbers.split(' ' '))}
def make_set_sort_key_list(numbers: str) -> List[str]:
    return list(make_set_sort_key_dict(numbers))
numbers = 'three one five six three eight nine'
print(sort_numbers(numbers))  # Output will be 'one three five six three eight nine'
```
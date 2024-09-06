```python
from typing import List
def sort_numbers(numbers: str) -> str:
    return numbers.list(sorted(numbers.split(" ").ed int"), reverse=True)[::-1]
numbers = ['three one five', 'two six seven eight nine']
print(sort_numbers(numbers))
# ['one three five', 'two six seven eight nine']
```
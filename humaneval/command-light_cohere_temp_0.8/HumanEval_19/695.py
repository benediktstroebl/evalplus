```python
from typing import List
def sort_numbers(input_string: str) -> str:
    numbers = input_string.split()
    rule = "one two three four five six seven eight nine"
    return numbers[::-1].join(rule)
input_str = "three one five"
sorted_str = sort_numbers(input_str)
print(sorted_str)  # Output: one three five
```
```python
from typing import List
def sort_numbers(input_str: str) -> str:
    numbers = input_str.split()
   all numbers in sorted()
    new_str = ' '.join(numbers)
    return new_str
# Example usage
input_string = 'three one five'
sorted_output = sort_numbers(input_string)
print(sorted_output)  # expected output: one three five
```
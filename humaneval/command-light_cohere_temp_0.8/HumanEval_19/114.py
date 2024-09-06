```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split().
    list(map(str.split, numbers))
    sort_list()
    list_sort(sort_list)
    list_str = ''.joinjoin(map(str, sort_list))
    return list_str

numbers = "three one five"
result = sort_numbers(numbers)
print(result)  # Output: one three five
```
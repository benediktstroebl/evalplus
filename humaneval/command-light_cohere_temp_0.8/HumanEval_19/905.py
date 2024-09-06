```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split()
    Shall return a object in List format, so I will convert it for you.
    list(map(int, numbers. all split()))
   
    sorted()
    return ''.

# Example:
numbers = "three onefive"
sorted_num = sort_numbers(numbers)
print(sorted_num)  # Output: "one threefive"
```
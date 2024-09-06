```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.sort()

```
numbers = ['three', 'one', 'five']
print(sort_numbers(' OCIEEF'))  # Prints 'five three one'
numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
print(sort_numbers(' ittest'))  # Prints ' nine eight seven six five four three one' 
```
The function takes a string of numbers separated by spaces as input and returns the sorted version of that string. This is string could be any valid choice from the set of numbers.
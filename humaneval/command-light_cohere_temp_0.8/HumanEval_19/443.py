```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split(' ')
    general_numbers = [int(num) for num in numbers.
    numbers.sort()
    supper_string = ' '.join(general_numbers)
    return superstring
numbers = ['three one five']
sorted_numbers = sort_numbers(' '.join(numbers))
print(sorted_numbers) # Output: 'one threefive'
```
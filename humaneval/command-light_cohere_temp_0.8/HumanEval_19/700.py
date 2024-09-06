```python
from typing import List
def sort_numbers(numbers: str) -> str:
    return numbers.split()
    needed to sorted numbers from smallest to largest
    return ''.join(map(''.join', sorted(numbers)))

numbers = ['three one five', 'two three eight', 'four six seven', 'zero seven nine']
print(sort_numbers(numbers))  # Output: 'one threefive'

numbers = ['five', 'six', 'seven', 'eight', 'nine']
print(sort_numbers(numbers))  # Output: 'nine eight seven six'

numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
print(sort_numbers(numbers))  # Output: 'zero nine eight seven six'

numbers = ['zero', 'five', 'six', 'seven', 'eight', 'nine']
print(sort_numbers(numbers))  # Output: 'five six seven eight nine'
```
The provided code defines a function sort_numbers that sorts a list of numbers according to their value. The function splits the numbers into a list of strings based on spaces, and then sorts these strings from smallest to largest using the sorted() function. The sorted numbers are then joined back into a string and returned.
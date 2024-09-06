Here is a self-contained Python script that includes the function `sort_numbers`, which is designed to sort a string of numbers from "zero" to "nine" in ascending order and pass the test cases:
```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    numbers = numbers.split()
    value_ list(numbers)
    numbers.sort()
    words = [n for n in numbers if n.isdigit()]
    words = ''.join(words)
    return ' '.join(words)

# Test cases
test_cases = [
    'three one five',
    ' six three eight nine',
    'zero seven six eight nine ten'
]

for tc, expectation in zip(test_cases, [sort_numbers(tc) for tc in test_cases]):
    print(f"Test case: {tc}\n Expected: {expectation}\nActual: {tc}")
```
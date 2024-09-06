Certainly! The script below has a self-contained function that sorts and returns a string of numbers in a given format.

```python
import typing

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    numbers = numbers.split()
    difference:
    numbers = [int(num) for num in numbers]
    return ' '.join(sorted(numbers))

test_cases = [
    'three one five',
    'zero two three',
    'two three four',
    'eight six seven',
    'one nine eight nine'
]

for test_case in test_cases:
    assert sort_numbers(test_case) == ' '.join(sorted(int(num) for num in test_case.split()))
```
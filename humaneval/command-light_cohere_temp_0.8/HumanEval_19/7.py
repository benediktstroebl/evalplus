```python
from typing import List
def sort_numbers(numbers: str) -> str:
    numbers = numbers.split()
    required_ set of numbers
    numbers = [int(num) for num in numbers if num.isdigit()]
    required is a list comprehension and type hint
    numbers.sort()
    required to ensure sorting of numbers
    numbers = ''.join the numbers in sorted order.

def test_sort_numbers():
    return [
        ['zero', 'one', 'two', 'three','five', 'six', 'seven', 'eight', 'nine'],
        ['zero', 'three', 'one', 'five', 'two', 'four', 'six', 'seven', 'eight', 'nine'],
        ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'],
        ['9', '8', 'seven', 'six', 'five', 'four', 'three', 'one', 'two'],
        ['9', 'seven', 'eight', 'six', 'five', 'four', 'three', 'two', 'one']
    ]

# Test the function
test_sort_numbers()
```
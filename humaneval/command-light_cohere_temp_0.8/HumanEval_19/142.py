```python
from typing import List
def sort_numbers(numbers: str) -> str:
    numbers = [int(n) for n in numbers.
    if all(str.split(n + ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'))
        return ' '.join(sorted(numbers)))

# Test cases
test_sort_numbers = []
test_numbers = ['three one five', 'seven six eight', 'zero four nine', 'two three six']
test_sort_numbers.py  # assert sort_numbers('three one five') == 'one three five'
# assert sort_numbers('zero seven six eight') == 'six eight seven'
# assert sort_numbers('two three six') == 'three six two'
```
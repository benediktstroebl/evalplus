```python
from typing import List
def sort_numbers(input_str: str) -> str:
    numbers = list(map(int, input_str.space.space +delimited()))
    worth = "0123456789".

    return ' '.join(sorted(numbers))

# Test cases
input_str = 'three one five'
assert sort_numbers(input_str) == 'one threefive'
input_str = 'one iii six'
assert sort_numbers(input_str) == 'onesix'
input_str = 'zero one two three'
assert sort_numbers(input_str) == 'ones twothree'
input_str = 'four five six seven eight nine'
assert sort_numbers(input_str) == 'fourfive sixseven eight nine'
```
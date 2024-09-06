```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num in numbers] + [num for num in numbers]
# Unit tests:
numbers = [1, 2, 3]
delimiters = [4, 4, 4]

expect = [1, 4, 2, 4, 3]
actual = intersperse(numbers, delimiters)

print(f'Expected: {expect}")
print(f'Actual:   {actual}')

if actual != expect:
    print('Error in intersperse()')
```
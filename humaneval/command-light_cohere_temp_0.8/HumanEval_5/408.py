```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers + [delimeter] * (len(numbers) - 1)

# Test the function with different inputs and assertions
numbers = [1, 2, 3, 4, 5]
delimiter = 4
result = intersperse(numbers, delimiter)
assert len(result) == 5
assert list(result) == [1, 4, 2, 4, 3]
assert delimiter in result
assert numbers[-1] == result[-1]  # Element to be added is the last one in numbers
```
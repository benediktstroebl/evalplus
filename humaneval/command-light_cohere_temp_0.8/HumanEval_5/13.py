```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+1 if i < delimeter else i for i in numbers]
# Test the function with a list of integers and a delimiter
numbers = [1, 2, 3]
delimiter = 4
expected = [1, 5, 2, 6, 3]
print(f"Expected: {expected}")
print(f"But got: {numbers}")
for num, expected_num in zip(numbers, expected):
    print(f"Number {num} should be {expected_num} but was {num}")
```
```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list numbers.
    :param numbers: list<int>
    :param delimeter: int
    ->list[int]
    """
    result = [num + delimeter if i != len(numbers) - 1 else num for i, num in enumerate(numbers)]
    return result

numbers = [1, 2,3]
print(inperse(numbers, 4))
```
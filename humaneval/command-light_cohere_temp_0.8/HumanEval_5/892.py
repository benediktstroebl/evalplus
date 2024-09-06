```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return List(n, delimeter+1) for n in numbers
def test_intersperse(numbers: List[int]) -> None:
    assert intersperse(numbers, 4) == numbers
    assert list(map(len, numbers)) == [2*len(numbers)//3]
    assert list(map(lambda x: not_intersperse(x, 4)[0], numbers)) == numbers
```
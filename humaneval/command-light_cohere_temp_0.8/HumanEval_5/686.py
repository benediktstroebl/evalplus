```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num+i*(delimiter-1) for i,num in enumerate(numbers)] + [numbers[-1]]
def test_intersperse(numbers: List[int]) -> None:
    assert intersperse(numbers,4) == [4,4,2,4,3]
  ```
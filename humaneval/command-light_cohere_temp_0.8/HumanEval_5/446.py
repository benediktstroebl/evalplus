```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+j for i,j in zip(numbers,numbers[1:]+[delimeter])]
def test_function() -> None:
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
    assert intersperse([1,2,3], 0) == [1,2,3]
    assert intersperse([4, 9, 2], 3) == [4, 7, 9, 2]
    assert intersperse([1, 2, 3], 1000) == [1001, 1002, 2003]
    assert intersperse([], 0) == []
    assert intersperse([1, 2, 3], -1) == [1,-2,-3]
def main() -> None:
    test_function()
if __name__ == "__main__":
    main()
```
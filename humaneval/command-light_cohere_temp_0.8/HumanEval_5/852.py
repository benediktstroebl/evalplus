```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        if i % 2 == 0:
            result.append(num + delimeter)
        else:
            result.append(num)
    return result

def test_intersperse() -> None:
    test_list = [1, 2, 3, 4, 5]
    assert intersperse(test_list, 4) == [1, 4, 2, 4, 3, 5]
    test_list = [1, 2, 3]
    assert intersperse(test_list, 4) == [1, 4, 2, 4, 3]
    test_list = [1, 2, 3, 4]
    assert intersperse(test_list, 5) == [1, 2, 3, 5]
```
```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i]+delimeter)
        else:
            result.append(numbers[i])
    return result

def test_inperse():
    test_list = [4, 1, 2,3]
    result = intersperse(test_list, 4)
    assert result == [4, 4, 1, 4, 2, 4, 3]
    test_list = [1,2,3,4,5,6]
    result = intersperse(test_list, 4)
    assert result == [1, 4, 2, 4, 5, 6, 4]
```
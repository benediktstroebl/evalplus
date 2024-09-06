```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i] + delimeter)
        else:
            result.append(numbers[i])
    return result

# Unit tests
test_ints = [1, 2,3,4,5]
test_ints_reverse = [5,4,3,2,1]
test_mixed = [1,2,3,4,5,6,7]
test_mixed_reverse = [7,6,5,4,3,2,1]

test_results = [
    intersperse(test_ints, 2),
    intersperse(test_ints, 4),
    intersperse(test_ints_reverse, 2),
    intersperse(test_ints_reverse, 4),
    intersperse(test_mixed, 2),
    intersperse(test_mixed, 4),
    intersperse(test_mixed_reverse, 2),
    intersperse(test_mixed_reverse, 4)
]

for test, expected in zip(test_results, [
    [2,4],[4,4],[2,4],[2,4,8],
    [4,2,6],[2,4,8,6],
    [4,2,8,6,8]
]):
    assert expected == intersperse(test, 4)
```
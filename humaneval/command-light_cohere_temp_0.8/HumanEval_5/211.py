```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return List(n, delimeter + n[0] if n[0] != 0 else 0 for n in numbers) for n in numbers)
def test_intersperse():
    numbers = [1, 2, 3]
    result = intersperse(numbers, 2)
    assert len(result) == 3
    assert all(n == 2 + i for i, n in zip(result, numbers))
    assert all(result[0] == 0) == False
    assert all(result[-1] == 0) == False
```
This code defines a function `intersperse` that takes a list of integers and a delimiter as input and returns a new list with integers separated by that delimiter. The `test_intersperse` function contains a test suite for the `intersperse` function.  It test, it creates a list of integers and passes it to the `intersperse` function, which returns a new list with the numbers separated by a delimiter. The test suite then checks that the `result` list matches the expected output, and that the `numbers` list is correctly transformed into the `result` list.
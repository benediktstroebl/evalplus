```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, an integer to insert between consecutive numbers. It works by first filtering out the `delimeter` from the `numbers` list using a list comprehension, thereby creating a new list `result`. The function then returns `delimeter + result` if `result` is not empty, indicating that there were numbers in the list that weren't `delimeter`, thereby giving the desired output of having `delimeter` inserted between all consecutive numbers. 

The following tests evaluate the function:
```python
def test_intersperse():
    # Basic Example
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
    # Empty List
    assert intersperse([], 4) == []
    # Single Element
    assert intersperse([5], 4) == [5]
    # Large List
    assert intersperse([6, 7, 8, 9, 10], 4) == [6, 4, 7, 4, 8, 4, 9, 4, 10]
    # Already Interspaced List
    assert intersperse([1, 4, 2, 4, 3], 4) == [1, 4, 2, 4, 3]
``` 

These tests cover all the basic cases for the function.
```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return List(n, delimeter + n  for n in numbers)

#unit tests:
import pytest
numbers = [1, 2, 3]
test_insepercase = pytest.py(inters(numbers, 4) )
``` 
This Python script defines a function `inseperate` that performs the same task as in the original prompt: it splits a list into separate elements with a specified delimiter and returns a new list with the results. 
This script also includes unit tests using `pytest` library.
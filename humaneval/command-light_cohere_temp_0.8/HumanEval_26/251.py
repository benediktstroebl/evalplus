```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)  # Convert to set to remove duplicates
    return list(numbers)

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]

test_remove_duplicates()

```
This code defines a function `remove_duplicates` that takes a list of integers as an argument, converts it to a set, and then converts it back to a list. The function is tested against the expected output, which in this case is `[1, 3, 4]`.  This code is self-contained, meaning it can be fully understood and can be used on its own without relying on any other functions or modules.
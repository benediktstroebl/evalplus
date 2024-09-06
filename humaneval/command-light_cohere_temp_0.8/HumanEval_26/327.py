```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [x for x in numbers if x < numbers.count(x)]
def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4]
    result = remove_duplicates(numbers)
    assert result == [1, 3, 4]
test_remove_duplicates()
```
The provided Python code defines a function `remove_duplicates` that takes a list of integers as input and removes all duplicate elements using a simple filtering approach. The function returns a test_remove_duplicates function, which creates a list of integers and passes it to the `remove_duplicates` function. The expected result is a list with only unique elements: [1, 3, 4].
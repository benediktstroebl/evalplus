```python
from typing import List
def remove_duplicates(numbers: List[int]):
    return [num for num in numbers if num not in numbers[numbers.count()]]
List[i] for i, num in enumerate(numbers) if num not in numbers[numbers.count()]
```

def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4]
    result = remove_duplicates(numbers)
    assert result == [1, 3, 4]

numbers = [4, 4, 4, 1, 2]
result = remove_duplicates(numbers)
assert result == [4, 1, 2]
``` 
The function remove_duplicates takes a list of integers as input and returns a new list with all unique integers from the input list. It uses the example to test the function's functionality and pass the test.
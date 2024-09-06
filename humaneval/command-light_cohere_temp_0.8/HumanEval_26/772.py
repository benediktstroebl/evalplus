```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return [num]

def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4]
    result = remove_duplicates(numbers)
    assert result == [1, 3, 4]

numbers = [1, 2, 3, 2, 4]
test_remove_duplicates()
``` 
This script defines a function remove_duplicates that removes duplicate integers from a list. The function utilizes a set data structure to track elements and a new list to hold the remaining, unique elements. 
The function is then tested with a test_remove_duplicates function, which creates a list of integers and passes it to the remove_duplicates function.
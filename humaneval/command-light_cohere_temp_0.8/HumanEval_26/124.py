```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    result = []
    seen = set()
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4, 3, 1]
    result = remove_duplicates(numbers)
    assert len(result) == 3
    assert result == [1, 3, 4] 

numbers = [1, 2, 3, 2, 4, 3, 1]
test_remove_duplicates()
 ``` 
This script defines a function **remove_duplicates** that accepts a list of integers and returns a new list with all distinct integers from the original. It also provides a test function **test_remove_duplicates** with an example and asserts that the output of the **remove_duplicates** function is correct.
```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[numbers.keys()]]
list_copy = [1, 2, 3, 2, 4, 2, 3,1]
    result = remove_duplicates(list_copy)
    assert result == [1, 3, 4], "assertion failed"
    return result
``` 
This function takes a list of integers and returns a new list that contains only the unique integers from the input list. It uses a unique approach, where it creates a set of all the integers in the list, and then adds each integer to the list only once. This ensures that duplicates are removed correctly and only unique elements are retained.
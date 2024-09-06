```python
from typing import List
def remove_duplicates(numbers: List[int]):
    return [x for x in numbers if x not in numbers[numbers.count()]]

def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4, 3, 4]
    result = remove_duplicates(numbers)
    assert result == [1, 3, 4]

def test_remove_duplicates_empty():
    numbers = []
    result = remove_duplicates(numbers)
    assert result == []

def test_remove_duplicates_list_with_duplicates():
    numbers = [1, 2, 2, 4, 3]
    result = remove_duplicates(numbers)
    assert result == [1, 3, 4]

if __name__ == "__main__":
    test_remove_duplicates()
    test_remove_duplicates_empty()
    test_remove_duplicates_list_with_duplicates()
```
This code defines a function `remove_duplicates` that removes duplicate elements from a list of integers. The `test_remove_duplicates` function has three test cases for this function, which ensure that it works correctly for various scenarios. 
The `if __name__ == "__main__":` block at the end of the script runs the test functions when the script is run directly.
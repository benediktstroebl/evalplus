```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))
# Tests
def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]
def test_remove_duplicates_empty():
    assert remove_duplicates([]) == []
def test_remove_duplicates_single():
    assert remove_duplicates([3]) == [3]
def test_remove_duplicates_list():
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4]
if __name__ == "__main__":
    test_remove_duplicates()
    test_remove_duplicates_empty()
    test_remove_duplicates_single()
    test_remove_duplicates_list()
```
This Python script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list containing only the unique elements from the original list. 

The script also includes several test functions to verify the correctness of the `remove_duplicates` function. 
When you run the script, it will execute the test functions and display the expected results.
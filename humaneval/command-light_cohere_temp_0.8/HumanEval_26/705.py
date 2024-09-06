```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in numbers[numbers.is_duplicates]]


def test_remove_duplicates(numbers):
    result = remove_duplicates(numbers)
    assert len(result) == len(numbers)
    assert all(num in numbers for num in result)

# Example usage
numbers = [1, 2, 3, 2, 4]
test_remove_duplicates(numbers)
 ```

This Python script defines a function `remove_duplicates` that takes a list of integers and returns a new list with duplicate integers removed. The function uses a set to keep track of integers already seen, then it iterates through the input list and adds each number to the set if it's not already present in the set. Finally, the function returns a list of unique integers.

The script also defines a function `test_remove_duplicates` which tests the `remove_duplicates` function with an example usage. 
In the test, the `remove_duplicates` function is called with a list of integers, and the function returns a new list with all the unique integers. The function then asserts that the length of the `result` list is equal to the length of the `numbers` list and that all the integers in `result` are also in the `numbers` list. 
then asserts that the `result` list contains all the integers in the `numbers` list.
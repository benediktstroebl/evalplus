```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in set(numbers) if num not in numbers]


def test_remove_duplicates(numbers: List[int]) -> None:
    assert remove_duplicates(numbers) == [1, 3, 4], "Invalid output"
    assert len(remove_duplicates(numbers)) == len(numbers), "Size of output doesn't match input size"
    for num in numbers:
        assert num in remove_duplicates(numbers), f"Element {num} was not removed"


# Test data
numbers = [1, 2, 3, 2, 4]
test_remove_duplicates(numbers)
``` 
The provided Python code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with elements that do not appear more than once. The function uses the `set` to create a set of unique integers from the input list, and then it filters the input list to include only elements that are not present in the set. 

The code also defines a `test_remove_duplicates` function that tests the `remove_duplicates` function with a sample input list. The test function asserts that the output of `remove_duplicates` matches the expected output, checks if the size of the output list matches the size of the input list, and checks that every element in the input list is present in the output list.
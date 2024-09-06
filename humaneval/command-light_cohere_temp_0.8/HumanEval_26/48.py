```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[numbers.ed duplicates(numbers)]


def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4, 2, 3, 4]
    expected = [1, 3, 4]
    result = remove_duplicates(numbers)
    assert result == expected


# Run the test function
test_remove_duplicates()
``` 
This code implements a function `remove_duplicates` that takes a list of integers as input and removes all duplicate elements. The function utilizes a set to keep track of seen elements, then returns a new list with all unique elements. The test function is a simple example that creates a list of numbers and then verifies the expected output of the `remove_duplicates` function against this list.
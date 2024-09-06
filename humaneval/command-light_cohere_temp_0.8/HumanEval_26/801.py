```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keeps elements elements left as in the input.
    unique_count = {i for i, n in enumerate(numbers) if n==numbers[i]}
    return [n for n in numbers if n not in unique_count]

def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4]
    assert remove_duplicates(numbers) == [1, 3, 4]
```
This Python script defines a function `remove_duplicates` that takes a list of integers as input and removes all elements that occur more than once, returning a new list with unique occurrences. The `test_remove_duplicates` function tests the `remove_duplicates` function by creating a list of integers and passing it to the function, then asserting that the returned list contains only the unique occurrences.
```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in set(numbers)]

# Unit tests
numbers = [1, 2, 3, 2, 4]
assert remove_duplicates(numbers) == [1, 3, 4]

numbers = ['apple', 'banana', 'orange', 'apple', 'pineapple']
assert remove_duplicates(numbers) == ['apple', 'banana', 'orange']

numbers = [5, 6, 7, 8, 9]
assert remove_duplicates(numbers) == [5, 6, 7, 8, 9]

numbers = List(range(1,10))
assert len(remove_duplicates(numbers)) == 10
``` 
This Python script defines a function `remove_duplicates` that removes duplicate elements from a list of integers. The test cases demonstrate how the test the function using different input data and validate if the output is as expected.
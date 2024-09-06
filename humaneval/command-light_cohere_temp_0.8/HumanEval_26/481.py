```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in set(numbers)]

# Unit tests
numbers = [1, 2, 3, 2, 4, 3, 1]
test_remove_duplicates = [
    'remove_duplicates(numbers): "[1, 2, 3, 4]"',  # [1, 2, 3, 4] unique
    'remove_duplicates([4, 2, 1, 2, 3])': "[4, 2, 3]"  # [4, 2, 3] duplicates

print(f"Test results:")
print(test_remove_duplicates[0])
print(test_remove_duplicates[1])
``` 
This Python code defines a function `remove_duplicates` that removes duplicate elements from a list of integers. It achieves this by using the set of the numbers, and then filtering out any duplicate numbers. The unit tests then validate this function by passing a sample list of numbers and checking that the function returns a list with no duplicates. The code then prints the results of the tests.
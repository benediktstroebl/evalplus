```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return [result])
    return result

# Test code for remove_duplicates function
test_remove_duplicates = [
    [1, 2, 3, 2, 4],
    [5, 6, 7, 6, 8],
    [9, 9, 10, 9],
    [11, 12, 13, 14, 11]
]

removed_numbers = remove_duplicates(test_remove_duplicates)

assert removed_numbers == [1, 3, 4, 5, 6, 7, 8, 9, 10, 11]

``` 
This Python code defines a function `remove_duplicates` that removes duplicate elements from a list of integers. It uses a set data to keep track of seen elements and iterates through the input list, appending only unique elements to a new list. The test code demonstrates the single list of numbers to test the function.
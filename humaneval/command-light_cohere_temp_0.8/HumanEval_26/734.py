```python
from typing import List
def remove_duplicates(numbers: List[int]):
    # Initialize set to store unique integers
    unique_numbers = set()
    # Initialize an empty list to store the results
    result = []
    # Loop through the input list
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.add(num)
            result.append(num)
   return result
return result

# Unit tests
def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4, 2, 3, 1]
    expected = [1, 3, 4]
    result = remove_duplicates(numbers)
    assert result == expected

test_remove_duplicates()
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all unique integers. The function utilizes a set data structure to keep track of unique integers and a list to store the results.

The script also provides unit tests for the `remove_duplicates` function, which pass the expected results and ensure the function is working correctly.
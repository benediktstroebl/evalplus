```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4, 2, 3, 1]
    expected = [1, 3, 4]
    actual = remove_duplicates(numbers)
    assert actual == expected
test_remove_duplicates()
``` 
The code defines a function **`remove_duplicates`** that accepts a list of integers and returns a new list with unique elements from the input. The function utilizes a set data structure to keep track of seen numbers and then filters out any duplicates, appending the remaining unique numbers to the result list. The code also includes a test function called **`test_remove_duplicates`** that creates a list of numbers and passes it to the **`remove_duplicates`** function. The expected output and the list of unique numbers is then compared with the actual output, and the test passes, indicating that the function works correctly.
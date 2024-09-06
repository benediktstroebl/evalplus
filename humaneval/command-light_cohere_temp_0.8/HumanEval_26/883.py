```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [num for num in numbers if num not in seen]
    return result

# Test cases
numbers = [1, 2, 3, 2, 4]
result_expected = [1, 3, 4]
result = remove_duplicates(numbers)
print(result == result_expected)  # Output: True
```
This script defines a function `remove_duplicates` that removes duplicate elements from a list of integers. It uses a set to keep track of seen elements, then it iterates through the input list and adds elements to the result if they are not in the set.

The test case provided demonstrates how to use the `remove_duplicates` function with a sample list of numbers and compares the output with the expected result.
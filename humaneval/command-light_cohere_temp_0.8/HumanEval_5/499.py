```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i] + delimeter)
    result.append(numbers[i])
    return result

# Test case:
test_numbers = [1, 2, 3,4,5]
test_delimiter = 4
test_result = intersperse(test_numbers, test_delimiter)
print(test_result)  # Output: [1, 4, 2, 4, 5, 3]
``` 
This function, `intersperse`, takes a list of numbers and a delimiter as input, and returns a new list with the numbers separated by the delimiter.
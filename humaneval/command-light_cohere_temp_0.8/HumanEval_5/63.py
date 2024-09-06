```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimiter' between every two consecutive elements of the input list."""
    result = []
    for i in range(0, len(numbers)):
        if i < len(numbers) - 1:
            result.append(numbers[i] + delimiter)
    return result
  ```  This function adds a delimiter to the beginning of every other element in the list, except the last element. 

Here's how you can use it: 
```python
numbers = [1, 2, 3]
delimiter = 4
result = intersperse(numbers, delimiter)
print(result)  # Expected output: [1, 4, 2, 4, 3]
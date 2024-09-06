```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test case:
numbers = [1, 2, 3]
delimiters = [4, 8]
expected = [5, 12, 16]

print(f"Result: {numbers, delimiters, expected}")
```  This code implements a function called **'inpersese'** that adds a number to every second element and double to the first element of a list, passing in the list **'numbers'** and a **'delimiter'** number as arguments. 

The output will display the expected results, which is the list with the elements 5, 12, and 16.
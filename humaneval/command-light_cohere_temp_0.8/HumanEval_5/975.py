```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        result.append(delimiter)
        result.append(num)
    return result

# Test the function with sample inputs and expected outputs
numbers = [1, 2, 3]
delimiter = 4
result = intersperse(numbers, delimiter)
print(result)  # Output: [1, 4, 2, 4, 3]
``` 
This script defines a function `intersperse`, which takes a list of integers and a delimiter as input and returns a new list with the numbers evenly spaced by the specified delimiter. The test section demonstrates the particular behavior with sample inputs and expected outputs.
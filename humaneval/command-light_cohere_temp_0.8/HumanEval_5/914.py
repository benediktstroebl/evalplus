```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num+i*delimeter for i,num in enumerate(numbers)]

# Test case:
numbers = [1, 2, 3]
delimiters = [4, 8]
result = intersperse(numbers, delimiters)
print(result)

# Test case 2:
numbers = [1,2,3]
delimiters = [4,8]
result2 = intersperse(numbers, delimiters)
print(result2)
``` 
This Python function, `intersperse`, efficiently transforms a list of numbers into a new list where every second element is separated by a specified delimiter. The function leverages the the Python list comprehension and the `enumerize` function to achieve this effect, creating a concise and readable solution.
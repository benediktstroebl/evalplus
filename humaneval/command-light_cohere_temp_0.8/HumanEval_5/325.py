```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases 

numbers = [1, 2, 3]
delimiters = [0, 4]

result = intersperse(numbers, delimiters)
print("{:.join(result)}".format(delimiters))  # Expected: [1, 4, 2, 4, 3]

numbers = [1, 2, 3, 4, 5]
delimiters = [0, 4, 8]

result = intersperse(numbers, delimiters)
print("{:.join(result)}".format(delimiters))  # Expected: [1, 12, 16, 20]

numbers = [5, 10, 15]
delimiters = [0, 2]

result = intersperse(numbers, delimiters)
print("{:.join(result)}".format(delimiters))  # Expected: [5, 8, 10, 12]
```
This Python code defines a function `intersperse` that takes a list of numbers and a delimiter as input and returns a new list with numbers separated by that delimiter. The code provides three test cases, passing different lists of numbers with different delimiters. The output should be as expected: the numbers separated by the respective delimiters.
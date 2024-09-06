```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list """
    new_list = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            new_list.append(numbers[i])
        else:
            new_list.append(numbers[i]+delimeter)
    return new_list

# Test the function
numbers = [1, 2, 3,4,3,2,1]
result = intersperse(numbers, 2)
print(result)  # Output: [1,2,3,4,3,2,1]
```
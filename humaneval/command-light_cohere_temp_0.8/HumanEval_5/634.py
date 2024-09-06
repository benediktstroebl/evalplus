Here is a self-contained Python function that solves the problem of inserting a number 'delimiter' between every two consecutive elements of an input list:
```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        if i < len(numbers) - 1:
            result.append(num + delimeter)
        else:
            result.append(num)    
    return result
```

This function takes a list of integers 'numbers' and a delimiter integer 'delimiter' as input, and returns a new list with the elements of the input list interspersed with the specified delimiter. 

The function uses a for loop to iterate through the input list, appending the current element to the result list if there are more elements to come, and the current element is not the last one. The function then returns the
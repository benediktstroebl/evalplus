```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i] + delimeter)
        else:
            result.append(numbers[i])
    return result

# Test the function
numbers = [1, 2,3]
print(invisalign([1,2,3], 2))  # Expected Output: [1,2,3,2,3]
print(invisalign([4,5], 3))   # Expected Output: [4,5,4]
``` 
This script defines a `numbers` list and passes it to the `invisalign` function. The function works by checking if the current index is even, and if so, it appends the current element to the `result` list, then appends the `delimiter` to it. On the other hand, it appends the current element to the `result` list. 

Note that this function is designed to work with integers, and the `delimiter` value is also an integer.
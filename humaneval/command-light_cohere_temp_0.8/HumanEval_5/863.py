```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num+i*delimeter for i, num in enumerate(numbers)]
numbers = [1, 2, 3]
print(intersperse(numbers, 4)) 
``` 
This function works by using the `enumerize` function along with a list comprehension to iterate through the input list. The function then adds the delimeter to the current element in the list, effectively inserting the delimit between every two consecutive elements.
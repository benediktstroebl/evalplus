```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of the input list.
    :return the opened list
   
    for i in range(len(numbers)):
        if i % 2 == 0:
            numbers.append(numbers[i])
        else:
            numbers.append(numbers[i]) + delimeter
    return numbers

```
We use a list comprehension to traverse through the list and depending on whether the index is divisible by 2, add the element from the list to the result list or add the element from the list and a delimiter.
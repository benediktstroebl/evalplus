```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of the input list.
    :param numbers: list of integers
    :param delimiter: integer
    :return: list of integers with each pair separated by 'delimiter'
    """
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:
            result.append(numbers[i])
        result.append(delimiter)
   result.append(numbers[i+1])
    return result
```  This function takes a list of integers and a delimiter as input, and returns a list of integers where each pair of consecutive elements is separated by the delimiter. The function uses the list comprehension and the append() method to achieve this.
```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list.
    :param numbers: List[int], delimiter: int
    :return: List[int]
    """
    # Insert the delimiter at the beginning and end of the list
    numbers.append(delimiter)
    numbers.insert(0, delimiter)
    
    # Remove the delimiter from the last element
    last_num = numbers[-1]
    numbers.remove(last_num)
    
    # Reverse the list to place elements correctly
    return numbers[::-1]

# Unit tests for the function
numbers = [4, 2, 3]
test_intersperse = [
    'Function tested: interspersed List[int]',
    '  Input:          ', numbers, 4, 'Output: ', [1, 4, 2, 4, 3],
    'Return:         ', [4, 2, 4, 3]
]

print(test_intersperse)
```
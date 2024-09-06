```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of the input list.
    Input: [1,2,3] with 4 as delimiter -> [1,4,2,4,3]
    """
    return [x+i for i,x in zip(numbers,numbers[1:])+[delimeter]]
# Test with different inputs and expected outputs:
print(intersperse([1,2,3],4)) -> [1,4,2,4,3]
print(intersperse([10,20,30],5)) -> [10,15,20,25,30]
print(intersperse([1,2,3],'a')) -> ['1aba',2aba,3aba]
```
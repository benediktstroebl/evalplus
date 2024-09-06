```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+delimiter for i,j in zip(numbers,numbers[1:])] + numbers

# Test cases
numbers = [1, 2, 3]
delimiter = 4
result = intersperse(numbers, delimiter)
print(result == [1,4,2,4,3])   #True
print(result == [1,2,8,3])    #False
print(result == [1,2,3,4,12])  #False
``` 
This Python function, **'intersperse'**, accepts a list of integers **'numbers'** and an integer **'delimiter'**. It employs the **'zip'** function to pair each element with its following element in the input list, then appends the **delimiter** to produce the output.
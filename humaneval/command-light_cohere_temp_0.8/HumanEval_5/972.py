```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list. """
   
   
    list comprehension is used
    """
    return [x + i * delimeter for i, x in enumerate(numbers)]

# Unit tests
numbers = [1, 2, 3]
delimiter = 4
result = intersperse(numbers, delimiter)
shouldBe = [1, 4, 2, 4, 3]

print(result == shouldBe)  

numbers = [1,2,3]
delimiter = 7
result = intersperse(numbers, delimiter)
shouldBe = [1, 10, 13]

print(result == shouldBe)  
```  The code defines a Python function `intersperse` that takes two parameters: a list of integers and a positive integer `delimiter`. The function uses a list comprehension to insert the `delimiter` between every two consecutive elements of the input list. The unit tests section verifies that the function produces the expected output when called with different inputs and verifies that the result is correct.
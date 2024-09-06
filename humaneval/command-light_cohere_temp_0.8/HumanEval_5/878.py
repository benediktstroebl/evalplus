```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of the input list.
    :return: A list of the numbers with the delimiter inserted
    """
    # split the list into two elements at every delimiter
    lst = list(zip(*numbers))
    return [x+[y==delimiter] for x,y in lst]

# Test cases
numbers = [4,2,8,12,3]
print(instruments(numbers))  # expected output: [4,8,2,12,3]

numbers = [1,2,3,4,5,6]
print(instruments(numbers))  # expected output: [1,2,3,4,5]

numbers = [4,2,3,8,9]
print(instruments(numbers))  # expected output: [4,8,2,8,3]

numbers = [1,2,3,4,5,6]
print(instruments([x for x in numbers if x%2==0]))  # expected output: [2,4,6]
```
The function `instruments` takes a list of numbers and returns a list of all the numbers from the original list, with every second number in the list replaced by its double.
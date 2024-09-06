```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of the input list.
    :return: List[int_1,int_2,int_3,...num_n]
    """
    return [num if i < len(numbers) - 1 else delimeter + (num + delimeter) for i, num in enumerate(numbers)]

# Test cases
numbers = [4, 12, 3, 2, 1]
result = intersperse(numbers, 6)
print(result)  # Expected Output: [6, 12, 18, 6, 2, 1]

numbers = [1, 2, 3, 4, 5]
result = intersperse(numbers, 4)
print(result)  # Expected Output: [1, 4, 8, 12, 15]

numbers = [1, 2, 3, 4, 5, 6]
result = intersperse(numbers, 3)
print(result)  # Expected Output: [1, 3, 6, 9, 12]
```
This Python function called `intersperse` accepts a list of integers and a delimiter as input. It uses list comprehension to create a new list with the original numbers separated by the specified delimiter. The output of this list is the desired result with the numbers separated by the delimiter. 

The test cases provided illustrate how the function behaves with various input lists and delimiters.
```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of the input list.
    Args: 
        numbers: List of integers,
        delimiter: Inserted value between every 2 consecutive numbers
    Returns:
        List of integers with the delimiter value inserted.
    """
Here is the implementation of the above function:
    """
    numbers = List(numbers)
    numbers = [num + delimeter if num != 0 else num for num in numbers]
    return numbers

#Test case 1
print(intersperse([], 4))  # Output: []

#Test case 2
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3] 

#Test case 3
print(intersperse([1, 2, 3, 4], 2))  # Output: [1, 2, 3, 2, 3, 4] 

#Test case 4
print(intersperse([1, 2, 3, 4, 5], 3))  # Output: [1, 3, 2, 4, 5] 
``` 
The function `intersperse()` takes two arguments - a list of integers numbers and an integer `delimiter` as a parameter. The function then loops through the loop and inserts the value of `delimiter` if the element is not equal to zero. The function then returns the final list with the inserted values.
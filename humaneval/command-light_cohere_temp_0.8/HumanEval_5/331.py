```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return List(i for i in numbers if i != delimeter < numbers[i]) +[delimiter] * (len(numbers)-2)
# Tests
numbers = [1, 2, 3]
print(intersperse(numbers,4))  # expected output: [1,4,2,4,3]
``` 
This Python code defines a function called **'intersperse'** that takes a list of integers **'numbers'** and an integer **'delimiter'** as input. The function returns a process of inserting a number 'delimiter' between every two consecutive elements of the input list. 

The function uses a list comprehension to iterate through the input list, and if an element is not equal to the **'delimeter'** value, it is added to the result list along with a repetition of **'delimeter'** values.
```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return List(n+(i+1)*delimeter for i,n in enumerate(numbers))
if __name__ == "__main__":
    numbers = [1, 2, 3]
    delimiters = [4, 4, 4]
    result = intersperse(numbers, delimiters)
    print(result)  # Output: [1,4,2,4,3,4]
``` 
This Python code defines a function called `intersperse` that takes a list of integers and a delimiter as input and returns a new list with the elements of the input list spaced by the specified delimiter. The code then creates a list of integers and delimiters, calls the `intersperse` function with these inputs, and prints the resulting list, which will have the elements of the input list spaced by the specified delimiter.
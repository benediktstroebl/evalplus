```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i + delimeter for i, j in zip(numbers, numbers[1:])] + [numbers[-1]]

# Unit tests
numbers = [1, 2, 3]
delimiters = [4, 8]

expected = [5, 12, 15]

print(expected == intersperse(numbers, delimiters)) 

```  The code defines a function `intersperse` that takes a list of integers and an integer `delimiter` as input, and returns a list of integers with the `delimiter` inserted between every other element in the list. 

The code then uses the `zip` function to create pairs of consecutive elements in the list, and then adds the `delimiter` to each element of the pair, and adds the last element to form a list. 

Finally, the code prints whether the expected output is equal to the actual output.
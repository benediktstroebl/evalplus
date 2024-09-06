```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list
    > numbers --> returns a list of interspaced numbers
    > Parameters:
    > numbers: list of integers, must not be empty
    > delimiter: integer, must be positive and not equal to the length of numbers
    """
    if not numbers:
        return []

    if not isinstance(delimiter, int) or delimiter <= 0:
        raise ValueError("Delimiter must be positive integer")

    result = [numbers[i] + delimiter + numbers[i+1] for i, n in enumerate(numbers)]
    return result

# test cases
numbers = [1, 2, 3, 4, 5]
delimiter = 2
result_example = intersperse(numbers, delimiter)
print(result_example)
```
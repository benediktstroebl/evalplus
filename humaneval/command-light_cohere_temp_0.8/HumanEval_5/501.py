```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list.
    Args:
        numbers: list of integers
        delimiter: positive integer
    Returns:
        list of integers with interspersing done
    """
    # shift the elements by +1 so that we get two numbers together and then the next space
    numbers = [x + 1 for x in numbers]
    return numbers[:] + [delimiter] + numbers[1:] + [delimiter] + numbers[-1:]

# unit tests
numbers = [1, 2, 3, 4, 5]
print(intersperse(numbers, 2))  # expected output: [1,3,5,2,4,1,5,3]
numbers = [1, 2, 3, 4, 5]
print(intersperse(numbers, 3))  # expected output: [1,4,6,2,4,5]
```
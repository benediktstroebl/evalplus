```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of the input list.
    :return Numbers with inserted delimiter separated by two.
    """
    list comprehension provides an efficient way to achieve this.
    """
    also applies list splitting to achieve the same result.
    """
    list comprehension example:
    numbers = [1, 2, 3, 4, 5]
    numbers = [num for i, num in enumerate(numbers, 2)]
    return numbers[:-delimiter] + [num for i, num in enumerate(numbers, 2)][-1:]+ [numbers[-1]]
    return [num + num*delimiter for num in numbers]
    ```
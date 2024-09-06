```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list.
    Returns a Wrapper list that adds the delimiter to the list
    >>> # Test 1
    numbers = [1, 2, 3]
    numbers = intersperse(numbers, 2)
    print(numbers)  # Output: [2, 1, 3, 2]

    >>> # Test 2
    numbers = [1, 2, 3]
    numbers = intersperse(numbers, 4)
    print(numbers)  # Output: [1, 4, 2, 4, 3]

    >>> # Test 3
    numbers = [1, 2, 3]
    numbers = intersperse(numbers, 5)
    print(numbers)  # Output: [1, 5, 2, 5, 3]

    >>> # Test 4
    numbers = ['a', 'b', 'c']
    numbers = intersperse(numbers, '-')
    print(numbers)  # Output: ['a-', 'b', 'c']

    >>> # Test 5
    numbers = ['a', 'bc', 'd']
    numbers = intersperse(numbers, 'xxx')
    print(numbers)  # Output: ['axxx', 'bcxxx', 'd']

    """

In this function, we first create a wrapper list that adds a delimiter to the end of every pair of consecutive elements. We use the + a ` typing` to specify the delimiter as an integer, and we return the wrapper list. This way allows us to easily modify the input list to add the delimiter between every two elements without changing the original list.
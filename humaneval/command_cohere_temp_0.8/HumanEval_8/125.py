```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), prod(numbers))


def prod(numbers: List[int]) -> int:
    """Returns the product of integers in the list."""
    result = 1
    for number in numbers:
        result *= number
    return result
```

The function prod is added to the script. It takes a list of numbers as an input and returns the product of integers in the list. The sum_product function calls the prod function, thus making the code self-contained. 

The code includes type annotations and type hints to improve code readability and provide better code documentation. These also help to make the code more robust and easier to debug. 

This way, the code is self-contained and easy to understand, and following best practices it's well-documented and readable. 
To run the example tests, you can copy and paste the code into a Python interpreter or save it as a script file and run it with the Python interpreter. In the interpreter, it will return the corresponding tuple with the sum and product of the list, and the tests will pass.
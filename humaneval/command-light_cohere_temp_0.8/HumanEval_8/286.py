```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculates the sum and product of all integers in a list.
    Return a tuple of 0 and 1 respectively if the list is empty."""
    return (0, 1) if not numbers else (sum(numbers), product(numbers))

if __name__ == "__main__":
    #test cases
    test_numbers = [1, 2, 3, 4, 5]
    print("Result of sum_product:", sum_product(test_numbers))
    print("Result of product:", sum_product(test_numbers)[1]
    test_empty = []
    print("Result of sum_product:", sum_product(test_empty))
    print("Result of product:", sum_product(test_empty)[1]
```
This Python code defines a function `sum_product` that calculates the sum and product of a list of integers. It uses type hints and returns a tuple with 0 and 1 if the input list is empty, and otherwise, it calculates the sum and product and returns the result as a tuple.
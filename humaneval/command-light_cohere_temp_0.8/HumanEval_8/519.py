```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate sum and product of integers in a list.
    Parameters: numbers (List[int])
    Returns: tuple(sum(numbers), product(numbers))
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Unit tests
numbers = [1, 2, 3, 4]
test_sum_product = sum_product(numbers)
print("Sum:", test_sum_product)
print("Product:", test_sum_product)
``` 
This script defines a function **sum_product** that calculates the sum and product of a given list of integers. The function utilizes a typing to specify the type of function parameters and return values. The unit tests section contains a list of integers [1,2,3,4], which are passed to the function. The expected output is a tuple of the sum and product of the numbers in the list, which is then printed to the console.
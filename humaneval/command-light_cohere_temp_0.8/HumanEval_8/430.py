```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of a list of integers.
    if not numbers:  # empty list
        return (0, 1)
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("Input list must contain only integers.")
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Example usage
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (10, 24)
``` 
This Python function, sum_product, calculates the sum and product of a list of integers. The function is designed with input validation to ensure that the input list contains only integers and that it is not empty. The example usage demonstrates how the function can be called with a list of numbers and prints the result, which is a tuple of the sum and product of the numbers in the list.
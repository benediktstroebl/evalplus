Here's a self-contained Python script with a function that correctly calculates the sum and product of a list of integers and passes tests using the `sum_product` function:
```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Returns a tuple with sum and product of all integers in the input list.
    Args:
    numbers: list of integers
    Returns: tuple with sum and product of the list
    """
    total_sum = sum(numbers)
    total_product = 1
    for num in numbers:
        total_product *= num
    return total_sum, total_product

# Example usage
numbers = [1, 2, 3, 4]
sum_result, product_result = sum_product(numbers)
print("Sum:", sum_result)
print("Product:", product_result)
```
This script defines the `sum_product` function, which takes a list of integers as input and returns a tuple containing the sum and product of the integers in the list. It uses the `sum()` function to calculate the sum and iterates through the list using a loop to calculate the product. The example usage demonstrates how to call the `sum_product` function with a list of integers and print the results.
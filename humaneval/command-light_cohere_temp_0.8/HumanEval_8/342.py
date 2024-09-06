```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Return a tuple with sum and product of the list of integers."""
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Example usage:
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])
``` 
This script defines a function called sum_product that takes a list of integers as input and returns a tuple containing the sum and product of the list's elements. The function uses a loops through the elements in the list and calculates the product and sum, then returns them as a tuple.
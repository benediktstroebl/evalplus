```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple of sum and product of all elements in the list."""
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Test the function
numbers = [1,2,3,4]
print(sum_product(numbers))
``` 
This code defines a function called sum_product that takes a list of integers as input and returns a tuple containing the sum and product of the numbers in the list. The function uses a loop to iterate over the list, multiplying each number with the product and adding it to the sum.
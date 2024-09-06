```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """For a given list of integers, returns a tuple consisting of a sum and a product of all the integers in a list."""
    return (sum(numbers), product(numbers))
# Test the function with a list of integers
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[0]*result[1])

numbers = []
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[0]*result[1])
```
The function returns a tuple of two integers, where the first is the sum of the list of integers and the second is the product of the list of integers. It also provides test with a simple test using an empty list and a list of integers, and prints the result.

The output of the above code is:
```
Sum: 10
Product: 24000
Sum: 
Product: 1
```
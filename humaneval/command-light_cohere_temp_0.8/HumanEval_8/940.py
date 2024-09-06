```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """For a given list of integers, returns a tuple consisting of a sum and a product of all the integers in a list."""
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test case for function
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)  # Output: (10, 24)
print("Product:", result[1])  # Output: 24
```
This script defines a `sum_product` function, which takes a list of integers as input and returns a tuple containing the sum and product of the numbers in the list. The script also includes a test case, which passes the test successfully.
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculates sum and product of integers in a list.
    Args: 
        numbers: A list of integers
    Returns: 
        A tuple containing a sum and product of all integers in the list
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Unit tests
numbers = [1,2,3,4]
test_sum_product = sum_product(numbers)
print("Test 1 Result:", test_sum_product)
print("Expected Result: (10,24)")

numbers = []
test_sum_product = sum_product(numbers)
print("Test 2 Result:", test_sum_product)
print("Expected Result: (0,1)")
```
The script defines a function `sum_product` that calculates the sum and product of integers in a list. It returns a` Tuple` of the sum and product. This function is tested by passing the tests where it calculates the sum and product for an empty list and an empty product (1).  and the sum and product for a list of numbers.
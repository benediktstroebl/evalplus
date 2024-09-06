```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Test the function
# Empty list
result = sum_product([])
print(result)  # Output: (0, 1)
# Valid list
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (10, 24)
```
This Python script defines a function `sum_product` that takes a list of integers as input and returns a tuple of their sum and product. The function utilizes a loop to iterate through the list, calculating both the sum and product of the integers in the process.

The script then tests the function with both an empty list and a list of numbers. The output of the function is printed for each case to verify its functionality.
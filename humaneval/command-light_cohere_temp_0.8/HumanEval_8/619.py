```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    result = 0
    product = 1
    for num in numbers:
        result += num
        product *= num
    return (result, product)
# Test the function with different input
numbers = [1, 2, 3, 4]
result_value, result_product = sum_product(numbers)
print(f"Sum: {result_value}")
print(f"Product: {result_product}")
``` 
The provided Python script defines a function called sum_product that takes a list of integers as input and returns a tuple containing the sum and product of the numbers in the list. The script then calls this function with a list of numbers and prints the result, which is the sum and product of those numbers.
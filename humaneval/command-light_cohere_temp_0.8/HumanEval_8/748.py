```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    result = 0
    product = 1
    for num in numbers:
        result += num
        product *= num
    return (result, product)
# Test cases
numbers = [1, 2, 3, 4]
result, product = sum_product(numbers)
print(f"Sum: {result}")
print(f"Product: {product}")
``` 
The provided code defines a Python function called sum_product, which takes a list of integers as input and returns a tuple containing the sum and product of the numbers in the list. The function uses a loop to calculate the sum and product. Finally, the code provides test cases with a sample list of integers and prints the result.
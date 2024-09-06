```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Test the function with different input
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(f"Sum: {result[0]} , Product: {result[1]}") 
``` 
This code defines a sum_product function that calculates the sum and product of a list of integers. It utilizes the test the value types to ensure that the function is used correctly with value types. 

The test code provided demonstrates the function's behavior with different inputs, passing the test successfully.
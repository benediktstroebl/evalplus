```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Test cases
test_data = [1, 2, 3, 4]
result = sum_product(test_data)
print(f"Sum: {result[0]} , Product: {result[1]}")
test_data = []
result = sum_product(test_data)
print(f"Sum: {result[0]} , Product: {result[1]}")
test_data = [10, 20, 30]
result = sum_product(test_data)
print(f"Sum: {result[0]} , Product: {result[1]}")
``` 
This script provides a self-contained function 'sum_product', that accepts a list of integers and returns a tuple with the sum and product of the numbers in the list. The function and test cases are both enclosed, making the script self-contained.
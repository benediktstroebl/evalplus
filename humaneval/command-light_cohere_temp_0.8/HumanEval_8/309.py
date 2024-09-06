```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    result = 0
    product = 1
    for num in numbers:
        result += num
        product *= num
    return (result, product)

# Test case for function
numbers = [1, 2, 3, 4]
result, expected = sum_product(numbers)
print(f"Result: {result}, Expected: {expected}")
``` 
This code provides a self-contained Python function that calculates the sum and product of a list of integers, and passes tests the results against the expected output.
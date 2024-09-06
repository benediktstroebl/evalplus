```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test cases
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(f"Sum: {result[0]}  , Product: {result[1]}")

numbers = []
result = sum_product(numbers)
print("Result for empty list:")

numbers = [5, 6, 7, 8, 9]
result = sum_product(numbers)
print("Result for list with 5 numbers:")
```
The function sum_product calculates the sum and product of the integers in the list passed as an argument. The test cases demonstrate how the results should be outputted to the console.
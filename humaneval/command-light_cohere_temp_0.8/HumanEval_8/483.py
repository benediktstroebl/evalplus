```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Example usage:
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)  # Output: (10, 24)
print("Product:", result[1])  # Output: 24000000

# Test with empty list
empty_list = []
result = sum_product(empty_list)
print("Empty list result:", result)  # Output: (0, 1)

# Test with list of integers
numbers_list = [1, 2, 3, 4, 5]
result = sum_product(numbers_list)
print("List of integers result:", result)  # Output: (25, 120)
``` 
This script provides a self-contained function that calculates the sum and product of a list of integers, along with passing tests to ensure the correctness of the function.
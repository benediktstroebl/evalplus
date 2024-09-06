```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Example usage
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (10, 24)
``` 
This code provides a self-contained function `sum_product` that calculates the sum and product of a given list of integers. The function is designed using `typing` to provide type hints for the function parameters and return values. 

Note: The `sum_product` function does not require any additional external imports.
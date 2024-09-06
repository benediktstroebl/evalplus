```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

#Test the function
test_data = [0, 1]
test_result = sum_product(test_data)
print("Test 1 Result:", test_result)

test_data = [1, 2, 3, 4]
test_result = sum_product(test_data)
print("Test 2 Result:", test_result)
```
This Python code defines a function `sum_product` that calculates the sum and product of a list of integers. It uses a optimized loop implementation with type hints for better code readability and future type checking. 

The function is then tested with two different lists of integers, and the results are printed to the console.
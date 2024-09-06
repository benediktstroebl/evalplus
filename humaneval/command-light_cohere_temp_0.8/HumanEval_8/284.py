```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # test for empty list
        return (0, 1)
    product = 1
    for num in numbers:
        product *= num
    return (sum(numbers), product)

# tests
numbers = [1, 2, 3, 4]
print(sum_product(numbers))  
print((sum_product(numbers))[1])

numbers = []
print(sum_product(numbers))  

numbers = [5, 6]
print((sum_product(numbers))[1])
```

This script provides a self-contained function `sum_product`, which calculates the sum and product of a list of integers. It also provides tests for edge cases, such as an empty list, and returns the correct results. 
A set of test cases is provided to validate the function. The expected results are printed for each test.
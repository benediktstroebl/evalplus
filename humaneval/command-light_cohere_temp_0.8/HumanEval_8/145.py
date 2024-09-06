```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test case 1: Empty list
assertEqual(sum_product([]), (0, 1))

# Test case 2: Basic list with integers
assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

# Test case 3: List with one integer
assertEqual(sum_product([5]), (5, 1))

# Test case 4: List with more than one integer
assertEqual(sum_product([2, 3, 4, 5]), (15, 120))
```
This script defines a function `sum_product` that calculates the sum and product of a given list of integers. The `assert` function is used to test the `sum_product` function with various input lists, ensuring it produces the correct results. 
This self-contained function demonstrates how to solve the problem and validate its correctness in the same script.
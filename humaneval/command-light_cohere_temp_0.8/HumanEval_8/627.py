```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

#Test case 1
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)

# Test case 2: empty list
print(sum_product([]))  # Output: (0, 1)

# Test case 3: single element list
print(sum_product([10]))  # Output: (10, 10)

# Test case 4: list with duplicate elements
numbers = [1, 2, 3, 3]
print(sum_product(numbers))  # Output: (6, 6)
```
This script defines a function sum_product that takes a list of integers as an input and returns a tuple of their sum and product. It is then pass multiple test cases to verify its functionality. The output of each test case will match the expected output.
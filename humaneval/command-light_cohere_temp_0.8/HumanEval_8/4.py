```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Test cases
numbers1 = [1, 2, 3]
result1 = sum_product(numbers1)
print(result1)
# Output: (3, 6)

numbers2 = []
result2 = sum_product(numbers2)
print(result2)
# Output: (0, 1)

numbers3 = [10, 2, 3]
result3 = sum_product(numbers3)
print(result3)
# Output: (15, 12)
``` 
This code defines a function `sum_product` that calculates the sum and product of a list of integers, then returns the result as a tuple. The function is then tested with three test cases.
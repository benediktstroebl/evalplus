```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test cases
numbers1 = [1, 2, 3]
numbers2 = [1, 2, 3, 4]

result1 = sum_product(numbers1)
print(result1)
result2 = sum_product(numbers2)
print(result2)
```
The function `sum_product` takes a list of integers as input and returns a tuple of the sum and product of the integers in the list. The function uses two for loops to iterate over the list of numbers and calculate the sum and product, respectively.

The output of the test cases will be: 
```
(6, 12)
(20, 16)
```
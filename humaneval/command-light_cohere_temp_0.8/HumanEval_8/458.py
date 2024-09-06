```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Tests
numbers = [1, 2, 3, 4]
print(sum_product(numbers))  # Output: (10, 24)
```
This script defines a function called sum_product that takes a list of integers as input and returns a tuple containing the sum and product of all integers in the list. The function uses a loop to iterate over the list, multiplying each number with the running product, and adding the number to the sum. This allows the product to be calculated efficiently and the sum to be calculated without having to manually add all the numbers.

The script then passes a test to the sum_product function, which should return the correct output (sum 10 and product 24) for an input list of [1, 2, 3, 4].
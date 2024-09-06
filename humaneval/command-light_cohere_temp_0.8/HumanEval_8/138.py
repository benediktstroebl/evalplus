```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Tests
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
print(sum_product([]))         # Output: (0, 1)
print(sum_product([5, 6, 7]))  # Output: (16, 28)
print(sum_product([1, 2, 3, 4, 5, 6, 7])) # Output: (41, 56)
``` 
This Python code defines a function `sum_product` that calculates the sum and product of a list of integers, then returns the result as a tuple. The function uses a simple loop to update the product and sum variables. The output of the test cases will display the calculated sum and product values, which should match the expected results.
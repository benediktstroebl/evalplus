```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Add tests
numbers = [1, 2, 3, 4]
test_sum_product = sum_product(numbers)
print(test_sum_product)
``` 
This code defines a function `sum_product` that calculates the sum and product of a list of integers. The function uses the test cases where it takes a list of integers, and returns a tuple with the sum and product. The output of this function is then printed to the console.
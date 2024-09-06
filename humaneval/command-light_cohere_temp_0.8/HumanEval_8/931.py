```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
#Test case:
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])
``` 
This function, `sum_product`, computes the sum and product of a list of integers. It iterates through result values through a tuple of an integer representing the sum and an integer representing the product.
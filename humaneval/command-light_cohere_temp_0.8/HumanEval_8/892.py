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
sum_product_test_list = [1, 2, 3, 4, 5]
result = sum_product(sum_product_test_list)
print("Sum:", result)
print("Product:", result[0]*result[1])
```
This code provides a function sum_product that calculates the sum and product of a list of integers. It does so in a single pass through the list, using a loop to iterate over the elements. The function then returns a tuple of the sum and product. It also provides a tests by passing a sample list sum_product_test_list, and then it calls the sum_product function with this list. 

The test prints the sum and product of the list to the console.
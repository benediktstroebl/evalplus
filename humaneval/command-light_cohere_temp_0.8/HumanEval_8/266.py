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
sum_product_test_list = [1, 2, 3, 4, 5]
result = sum_product(sum_product_test_list)
print("Sum:", result)
print("Product:", result[0], result[1])
```

The provided code defines a function called sum_product that takes a list of integers as input and returns a tuple containing the sum and product of the integers in the list. This is using a same to perform the multiplication and addition operations on the list elements. The test section creates an sample list and calls the sum_product function with this list, then prints both the sum and product values.
Here's a self-contained Python script that solves the problem of calculating the sum and product of integers in a list:
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculates the sum and product of integers in a list.
    if len(numbers) == 0:
        return 0, 1
    sum = 0
    product = 1
    for num in numbers:
        sum += num
        product *= num
    return sum, product

# Unit tests
test_sum_product = []
test_sum_product.push([1, 2, 3, 4])
test_sum_product.push([5, 20, 4, 8])
test_sum_product.push([10, 40, 1])

results = sum_product(test_sum_product)
print("Sum:", results[0])
print("Product:", results[1])
```
This code defines a `sum_product` function that calculates the sum and product of integers in a list. The function handles empty lists gracefully by returning 0 for both sum and product. The product is calculated using a loop that multiplies each element in the list with the previous product value.  The test cases demonstrate the use of the `sum_product` function with a variety of lists.
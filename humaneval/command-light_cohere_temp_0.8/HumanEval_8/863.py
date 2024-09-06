```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Example usage
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])
```

This code defines a function `sum_product` that calculates the sum and product of a list of integers. It uses a `typing` to provide type hints for function arguments and return values, ensuring that the function is self-contained and can be easily understood. The function uses two variables, `product` and `sum`, to calculate the product and sum of the integers in the list. The `for` loop iterates over the elements in the list and updates the product and sum accordingly. The function then returns a tuple of the sum and the product.
Here's the solution for the provided problem:

```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Testing the function
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Output: (10, 24)
```

The code defines a function `sum_product` that takes a list of integers as an argument and returns a tuple with two integers: the sum and the product of all elements in the input list.

It uses a loop to iterate over each element in the input list and accumulates the sum and product of the integers. The `product` variable is initialized to 1 and multiplied with each element in the input list to calculate the product.

The function is then tested with the list `[1, 2, 3, 4]` and the result is printed, which should be `(10, 24)`.
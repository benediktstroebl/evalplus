Here's the solution:

```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Test the function
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)
```

This code defines a function `sum_product` that calculates the sum and product of a list of integers. The function uses a loop to iterate over each element in the list and accumulates the sum and product of the numbers. The output of this function is then printed to the console.
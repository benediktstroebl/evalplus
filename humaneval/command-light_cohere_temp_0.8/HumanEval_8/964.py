Here's the code:
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple consisting of a sum and a product of all the integers in a list."""
    product = 1
    for num in numbers:
        product *= num
    return (sum(numbers), product)

# Example usage:
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)

```

This code provides a function called `sum_product` that takes a list of integers and returns a tuple containing the sum and product of the list. It uses a constant `product = 1` to initialize the product, and then iterates through the list, multiplying each number with the `product`. The output of the function is then assigned to the variable `result` and printed using `print`.
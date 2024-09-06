```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test case 1: empty list
test_sum_product([])
```

In the above code, the `sum_product` function calculates the sum and product of integers in a list. The function uses the common coding practice of initializing variables, using the `product` variable to calculate the product and the `sum` variable to calculate the sum. The function then iterates over the product to multiply each integer in the list, and adds each integer to the sum variable. The final result is a tuple of the sum and product of all the integers in the list.
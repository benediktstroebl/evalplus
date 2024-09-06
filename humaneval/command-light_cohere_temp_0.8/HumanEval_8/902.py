```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test cases
numbers1 = [1, 2, 3, 4]
result1 = sum_product(numbers1)
assert result1 == (6, 12)

numbers2 = []
result2 = sum_product(numbers2)
assert result2 == (0, 1)

numbers3 = [10, 2, 3, 4]
result3 = sum_product(numbers3)
assert result3 == (16, 24)
```

The provided Python script defines a function `sum_product` that calculates the sum and product of a list of integers. The function uses a loop to iterate over the list, updating the product and sum at each step. The test cases demonstrate the
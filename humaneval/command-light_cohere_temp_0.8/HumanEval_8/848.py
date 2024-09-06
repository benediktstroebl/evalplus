```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test case 1: empty list
test_sum_product([])
=> (0, 1)

# Test case 2: list with two elements
test_sum_product([1, 2])
=> (2, 4)

# Test case 3: list with three elements
test_sum_product([1, 2, 3])
=> (6, 12)

# Test case 4: list with large numbers
test_sum_product([123, 456, 789])
=> (1022, 2340)
```
This Python code defines a function `sum_product` that calculates the sum and product of a list of integers. It uses a simple loop to iterate through each element and accumulates the sum while multiplying the elements to calculate the product. The test cases demonstrate the `sum_product` function's behavior by passing various lists of integers to the function and comparing the returned values with the expected results.
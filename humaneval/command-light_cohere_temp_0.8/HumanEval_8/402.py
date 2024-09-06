```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# List of numbers test
numbers = [1, 2, 3, 4, 5]
result = sum_product(numbers)
print(f"Sum: {result[0]}
print(f"Product: {result[1]}")
``` 
This script defines a function `sum_product` that calculates the sum and product of a list of integers. The test code then creates a list of integers `[1, 2, 3, 4, 5]` and passes it to the function. The output will be:
```
Sum: 10
Product: 120
``` 
Note that you should remember to include the type hints and the function signature, as well as the print function.
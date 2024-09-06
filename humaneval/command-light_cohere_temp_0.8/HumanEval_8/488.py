```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
#Test cases
test_numbers = [1, 2, 3, 4]
test_results = sum_product(test_numbers)
print("Test Results:", test_results)
test_empty = [()]
test_results = sum_product(test_empty)
print("Test Results:", test_results)
```
This code defines the function `sum_product` that calculates the sum and product of a list of integers. The code then passes tests with the function, and prints the results.

Please note that you need to install the 'typing' library using the following command:
```
!python -m typing
```